from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView


from .models import Article
from .serializers import ArticleSerializers


# Create your views here.

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializers(articles, many=True)
        return Response({'articles': serializer.data})

    def post(self, request):
        articles = request.data.get('articles')
        serializer = ArticleSerializers(data=articles)
        if serializer.is_valid(raise_exception=True):
            article_save = serializer.save()
        return Response({'Successes': "Article'{}' Created Successfully".format(article_save.title)})



class ArticleDetailView(APIView):
#     def put(self, request, pk ):
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('articles')
#         serializer = ArticleSerializers(instance=saved_article, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
#
#     def delete(self, request, pk):
#         # Get object with this pk
#         article = get_object_or_404(Article.objects.all(), pk=pk)
#         article.delete()
#         return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        article = self.get_object(pk)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    def put(self,request,pk):
        article = self.get_object(pk)
        serializer = ArticleSerializers(instance=article, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


