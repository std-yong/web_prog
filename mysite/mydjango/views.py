from django.shortcuts import render
from mydjango.models import Item

# Create your views here.

from django.http import HttpResponse

#클라이언트의 요청을 처리하는 함수
#이 함수의 매개변수는 HttpRequest 타입인데
#이 타입은 클라이언트의 정보를 가진 클래스이다
def index(request):
    print(Item)

    data = Item.objects.all()
    print(data)

    return render(request, 'index.html', {'data':data})

def detail(request, itemid):
    #itemid를 가진 데이터 찾아오기
    item = Item.objects.get(itemid=itemid)
    print(item)
    return render(request, 'detail.html', {'item':item})


from django.db.models import Max
from django.shortcuts import  redirect
def insert(request):
    #데이터 삽입화면으로 이동
    if request.method == 'GET':
        return render(request, 'insert.html')

    else:
        #itemid를 생성 - 가장 큰 itemid + 1
        #가장 큰 itemid 찾기
        obj = Item.objects.aggregate(itemid = Max('itemid'))
        if obj['itemid'] == None:
            obj['itemid'] = 0
        #가장 큰 itemid + 1
        itemid = int(obj['itemid']) + 1

        #파라미터 읽기
        itemname = request.POST['itemname']
        price = request.POST['price']
        description = request.POST['description']

        for img in request.FILES.getlist('pictureurl'):
            item = Item()
            item.itemid = itemid
            item.itemname = itemname
            item.price = price
            item.description = description
            item.pictureurl = img
            #데이터 삽입
            item.save()
        #삽입 삭제 갱신 작업 후에는 forwarding을 하지 않고 redirect
        return redirect('/')