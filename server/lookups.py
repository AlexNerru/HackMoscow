from ajax_select import register, LookupChannel
from .models import Tag

@register('tags')
class TagsLookup(LookupChannel):

    model = Tag

    def check_auth(self, request):
        return True

    def get_query(self, q, request):
        print(q)
        v = self.model.objects.filter(tagname__icontains=q.capitalize())
        if len(v) == 0:
            v = self.model.objects.all().order_by('tagname')
        return v

    def format_match(self, item):
        return item.tagname

    def format_item_display(self, item):
        return item.tagname
