from django import template

register = template.Library()

@register.filter
def replay(comment):
    if comment_rep := comment.comment_replay.filter(active=True):
        return comment_rep
