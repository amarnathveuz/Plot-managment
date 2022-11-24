from rest_framework import serializers

from .models import intractive_map,plot_view_master_image


class Intractive_mapSerializer(serializers.ModelSerializer):
    attachement_multiple_filea = serializers.SerializerMethodField()

    current_price_new = serializers.SerializerMethodField()

    plot_view = serializers.SerializerMethodField()
     
    class Meta:
        model = intractive_map
        # fields = ['id','title', 'author','email']
        fields = '__all__'
    def get_attachement_multiple_filea(self,obj):
        return obj.intractive_map_multiple_image_id.values('attached_file','image_type','image_name')
    
    def get_current_price_new(self,obj):
        
        
        status =  '{:20,.2f}'.format(obj.Price)
        status = str(status).replace(" ", "")

        return status
    
    def get_plot_view(self,obj):
        data = plot_view_master_image.objects.filter(mapping_id__unit_type=obj.UType)
        if data:
            return True
        else:
            return False

        

