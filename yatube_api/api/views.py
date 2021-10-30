from rest_framework import filters, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Follow, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_post(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post

    def get_queryset(self):
        post = self.get_post()
        queryset = Comment.objects.filter(post=post)
        return queryset

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(
            author=self.request.user,
            post=post
        )


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
