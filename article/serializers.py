from rest_framework import serializers

from article.models import Article, Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name',)
        
class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Article
