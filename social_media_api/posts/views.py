# posts/views.py
from rest_framework import viewsets, filters, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like # Import Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer # Import LikeSerializer
from .permissions import IsAuthorOrReadOnly
from notifications.models import Notification # Import Notification
from django.contrib.contenttypes.models import ContentType

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        
        # Check if user already liked the post
        if Like.objects.filter(user=user, post=post).exists():
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the Like object
        Like.objects.create(user=user, post=post)

        # Create a notification for the post's author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked',
            target=post
        )
        return Response({'status': 'post liked'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        
        # Try to delete the like object
        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response({'status': 'post unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

# ... (your existing UserFeedAPIView)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        # Create notification for the post's author when a comment is made
        Notification.objects.create(
            recipient=comment.post.author,
            actor=self.request.user,
            verb='commented on',
            target=comment.post
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserFeedAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        following_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data)
    def get(self, request):
        followed_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data)
    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'