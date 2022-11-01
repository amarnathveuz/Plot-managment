from rest_framework import serializers

from .models import intractive_map


class Intractive_mapSerializer(serializers.ModelSerializer):
    attachement_multiple_filea = serializers.SerializerMethodField()

    current_status_new = serializers.SerializerMethodField()
    class Meta:
        model = intractive_map
        # fields = ['id','title', 'author','email']
        fields = '__all__'
    def get_attachement_multiple_filea(self,obj):
        return obj.intractive_map_multiple_image_id.values('attached_file','image_type','image_name')
    
    def get_current_status_new(self,obj):
        status = ''
        
        if obj.current_status == '0':
            status = "availlll"
        elif obj.current_status == '1':
            status ="not avaaa"

        return status