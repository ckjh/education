# 章节列表
class SectionView(APIView):
    def get( self, request):
        mes = {}
        try:
            section = Section.objects.all()
            s = SectionSerializersModel(section,many=True)
            mes['code'] =200
            mes['message'] ='ok'
            mes['dataList'] =s.data
        except:
            mes['code'] =10010
            mes['message'] ='数据库请求失败'
        return Response(mes)

    def post( self, request):
        mes = {}
        data = request.data
        data[ 'video' ] = get_pic_url ( data[ 'video' ] )
        if data:
            s = SectionSerializers(data=data)
            if s.is_valid():
                s.save()
                mes[ 'code' ] = 200
                mes[ 'message' ] = 'ok'
            else:
                print(s.errors)
                mes[ 'code' ] = 10020
                mes[ 'message' ] = '添加失败'
        else:
            mes[ 'code' ] = 10030
            mes[ 'message' ] = '获取数据不全'
        return Response(mes)

    def put( self, request):
        data = request.data.copy ()
        data[ 'video' ] = get_pic_url ( data[ 'video' ] )
        print ( data )
        c1 = Section.objects.get ( id=data[ 'id' ] )
        ser = SectionSerializers ( c1, data=data )
        mes = {}
        if ser.is_valid ():
            ser.save ()
            mes[ 'code' ] = 200
            mes[ 'msg' ] = 'ok'
        else:
            print ( ser.errors )
            mes[ 'code' ] = 400
            mes[ 'msg' ] = '失败'
        return Response ( mes )

    def delete(self, request):
        id = request.data['id']
        mes = {}
        if id:
            Section.objects.get(id=id).delete()
            mes['code'] = 200
            mes['msg'] = "删除成功"
        else:
            mes['code'] = 400
            mes['msg'] = "删除失败"
        return Response(mes)




# 序列化 ...


# 章节序列化
class SectionSerializersModel(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


# 章节反序列化
class SectionSerializers(serializers.Serializer):
    course = serializers.IntegerField()
    section = serializers.CharField()
    video = serializers.CharField()
    sort = serializers.IntegerField()

    def create(self, data):
        m = Section.objects.create(**data)
        return m

    def update(self, instance, validated_data):
        instance.name = validated_data['course']
        instance.desc = validated_data['section']
        instance.pic = validated_data['video']
        instance.pic = validated_data['sort']
        instance.save()
        return instance
