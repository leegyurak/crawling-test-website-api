from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from blog.models import Post
from blog.pagination import PostPageNumberPagination
from blog.serializers import PostSerializer


class PostListRetrieveViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    pagination_class = PostPageNumberPagination
    queryset = Post.objects.all().order_by('-created_at')

    def list(self, request, *args, **kwargs):
        queryset = super().get_queryset()

        title = request.query_params.get('title')
        text = request.query_params.get('text')

        if title != '' and title is not None:
            queryset = queryset.filter(title__contains=title)

        if text != '' and text is not None:
            queryset = queryset.filter(text__contains=text)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)