

@register.filter

def started_time(created):
    return arrow.get(created_at).humanize()

@register.simple_tag
def last_posted_user_name(thread):
    posts = thread.posts.all().order_by('-created_at')
    return post[posts.count()-1].user.username