from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Item,Contact,Order,orderupdate
from math import ceil
import json
# from PayTm import Checksum

MERCHANT_KEY = 'kbzk1DSbJiV_O3p5';

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# Create your views here.
def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

# def index(requerst):
#     products=Product.objects.all()
#     # print(products)
#     # n=len(products)
#     # print(products)
#     # nSlides= n//4 + ceil((n/4)-(n//4))
    
#     allprods=[]
#     catprods=Product.objects.values('category','id')
#     cats={item['category'] for item in catprods}
#     for cat in cats:

#         prod=Product.objects.filter(category=cat)
#         n=len(prod)
#         nSlides= n//4 + ceil((n/4)-(n//4))
#         allprods.append([prod,range(1,nSlides),nSlides])
    
#     # params={ 'no_of_slide':nSlides,'range':range(1,nSlides),'product':products }
#     # allprods=[[products,range(1,nSlides),nSlides],
#     # [products,range(1,nSlides),nSlides]]
#         params={'allProds':allprods}
    
#         return render(requerst,'shop/index.html',params)
#     # return HttpResponse("index shop")


def contact(request):
    thank=False
    if(request.method == 'POST'):
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        phone1=request.POST.get('phone')
        query1=request.POST.get('query')
        contact=Contact(name=name1,email=email1,phone=phone1,desc=query1)
        contact.save()
        thank=True




        # print(name1,email1,phone1,query1)
        print(request)


    return render(request,'shop/contact.html',{'thank':thank})
    # return HttpResponse('contact')


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            print(orderId,email)
            if len(order)>0:
                print("we enter the leng")
                update=orderupdate.objects.filter(orderid=orderId)
                updates = []
                for item in update:
                    print(item.updatedesc,item.timestamp)

                    updates.append({'text': item.updatedesc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].iems_json], default=str)
                return HttpResponse(response)
            else:

                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request,'shop/tracker.html')





def search(requerst):
    return HttpResponse('search')


def product(request,myid):
    # fetch the product use the id
    products=Product.objects.filter(id=myid)  #this is list then i will write products[0]
    print(products)
    
    # print(name)
    return render(request,'shop/product.html',{'products':products[0]})
    # return HttpResponse('product')

def checkout(request):
    if(request.method=="POST"):
        itemJson=request.POST.get('itemsJson')
        name=request.POST.get('name1')
        email=request.POST.get('email')
        amount = request.POST.get('amount', '')
        address=request.POST.get('address')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip1=request.POST.get('zip1')
        phone=request.POST.get('phone')
        orders=Order(iems_json=itemJson,name=name,email=email,address=address,address2=address2,city=city,state=state,zip_code=zip1,phone=phone)
        print(name,email,address,address2,city,state,zip1,phone)
        orders.save()
        thank=True
        id=orders.order_id
        updateorder=orderupdate(orderid=id,updatedesc="you order his placed success full ")
        updateorder.save()
        # return render(request,'shop/checkout.html',{'thank':thank,'id':id})
        
        #paytm transfer to money 
        param_dict = {

                'MID': 'Your-Merchant-Id-Here',
                'ORDER_ID': str(orders.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        }
        # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        param_dict['CHECKSUMHASH'] =Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})

    return render(request,'shop/checkout.html')
    # return HttpResponse('checkout')

def about(requerst):
    return render(requerst,'shop/about.html')
    # return HttpResponse('about')

@csrf_exempt
def handlerequest(request):
    # paytm will send the request
    return HttpResponse('done')
    # pass

