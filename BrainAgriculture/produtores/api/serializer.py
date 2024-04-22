from rest_framework import serializers
from produtores.models import Cultura, Produtor
from validate_docbr import CPF, CNPJ


class CulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultura
        fields = ["nome"]

    def to_internal_value(self, value):
        if isinstance(value, str):
            return {"nome": value}
        return super().to_internal_value(value)

    def validate_nome(self, value):
        culturas_permitidas = ["Soja", "Milho", 'Algodão', "Café", "Cana de Açúcar"]
        if value not in culturas_permitidas:
            raise serializers.ValidationError(
                "Apenas as culturas Soja, Milho, Algodão, Café, Cana de Açúcar são permitidas.")
        return {'nome': value}

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data['nome']


class ProdutorSerializer(serializers.ModelSerializer):
    culturas = CulturaSerializer(many=True)

    class Meta:
        model = Produtor
        fields = [
            "id",
            "cpf_cnpj",
            "nome",
            "nome_fazenda",
            "cidade",
            "estado",
            "area_total_hectares",
            "area_agricultavel_hectares",
            "area_vegetacao_hectares",
            "culturas"
        ]

    def create(self, validated_data):
        culturas_data = validated_data.pop('culturas', [])
        produtor = Produtor.objects.create(**validated_data)
        for cultura_data in culturas_data:
            nome_cultura = cultura_data['nome']
            Cultura.objects.create(nome=nome_cultura, produtor=produtor)
        return produtor

    def update(self, instance, validated_data):
        # Atualizar os campos do Produtor
        instance.nome = validated_data.get('nome', instance.nome)
        instance.cpf_cnpj = validated_data.get('cpf_cnpj', instance.cpf_cnpj)
        instance.nome_fazenda = validated_data.get('nome_fazenda', instance.nome_fazenda)
        instance.cidade = validated_data.get('cidade', instance.cidade)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.area_total_hectares = validated_data.get('area_total_hectares', instance.area_total_hectares)
        instance.area_agricultavel_hectares = validated_data.get('area_agricultavel_hectares',
                                                                 instance.area_agricultavel_hectares)
        instance.area_vegetacao_hectares = validated_data.get('area_vegetacao_hectares',
                                                              instance.area_vegetacao_hectares)

        culturas_data = validated_data.pop('culturas', [])
        for cultura_data in culturas_data:
            nome_cultura = cultura_data['nome']
            if not instance.culturas.filter(nome=nome_cultura).exists():
                Cultura.objects.create(nome=nome_cultura, produtor=instance)

        instance.save()
        return instance

    def validate(self, data):
        if data['area_total_hectares'] < (data['area_agricultavel_hectares'] + data['area_vegetacao_hectares']):
            raise serializers.ValidationError(
                "A soma da área agricultável e da área de vegetação não pode ser maior que a área total da fazenda.")

        cpf_cnpj = data.get('cpf_cnpj')
        if cpf_cnpj:
            if len(cpf_cnpj) == 11:
                cpf_validator = CPF()
                if not cpf_validator.validate(cpf_cnpj):
                    raise serializers.ValidationError("CPF inválido.")
            elif len(cpf_cnpj) == 14:
                # Aqui você pode validar o CNPJ, se desejar
                pass
            else:
                raise serializers.ValidationError("CPF/CNPJ deve ter 11 ou 14 dígitos.")

        return data
