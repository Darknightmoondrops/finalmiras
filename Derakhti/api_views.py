from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from random import choices
from string import ascii_lowercase,ascii_letters
from django.shortcuts import get_object_or_404
from extensions.derakhti.amount_purchased import amount_purchased
import datetime


class contracts_add(generics.CreateAPIView):
    serializer_class = ContractsSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = ContractsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            contract_check = Contracts.objects.filter(user_id=token_info.user.id).first()
            if contract_check is None:
                contract_create = Contracts.objects.create(user_id=token_info.user.id)
                return Response({'created': contract_create.jdate()})
            else:
                return Response({'message': 'قرار داد از قبل تایید شده'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)


class cards_add(generics.CreateAPIView):
    serializer_class = CardsSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = CardsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            cards_check = Cards.objects.filter(user_id=token_info.user.id).first()
            if cards_check is None:
                data.save()
                data.instance.user = token_info.user
                data.save()
                return Response({'message': 'با موفقیت اضافه شد'})
            else:
                return Response({'message': ' از قبل اضافه شده'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)


class profile_update(generics.UpdateAPIView):
    serializer_class = UsersSerializers
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        data = UsersSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            user = Users.objects.filter(id=token_info.user.id).first()
            data.update(user,data.validated_data)
            return Response({'message': 'بروز شد'})
        else:
            return Response(data.errors)


class place_user_buy(generics.CreateAPIView):
    serializer_class = MainUserSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = MainUserSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            sub_categories_number = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True).count()

            user = Users.objects.filter(id=token_info.user.id).first()
            owner_check = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id).first()
            mainU = MainUser.objects.filter(user_id=token_info.user.id,payment_status=True).first()
            mainU_check = MainUser.objects.filter(user_id=token_info.user.id,payment_status=False).first()

            if mainU_check is None:
                if mainU is not None:
                    return Response({'message': 'کاربر قبلا  جایگاه انتخاب کرده است'})

                if owner_check is None:
                    return Response({'Owner': 'وجود ندارد'})
                else: pass

                mainR = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True,r_or_l=True).first()
                mainL = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True,r_or_l=False).first()

                if mainR is not None and data.validated_data['r_or_l'] == True:
                    return Response({'message': 'راست کاربر پر است'})
                elif mainL is not None and data.validated_data['r_or_l'] == False:
                    return Response({'message': 'چپ کاربر پر است'})
                else: pass

                mainU = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id).first()
                if data.validated_data['places'] == 1 and amount_purchased(token_info.user.id) >= 10005000:
                    data.save()
                    data.instance.user_id = token_info.user.id
                    data.instance.place = 1
                    data.instance.r_or_l = data.validated_data['r_or_l']
                    data.save()

                    mainU = MainUser.objects.filter(user_id=token_info.user.id).first()
                    mainU.payment_status = True
                    mainU.save()
                    #
                    # main_check = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True).count()
                    # if main_check == 1:
                    #     user = Users.objects.filter(id=data.validated_data['Owner'].id).first()
                    #     user.commission += 120000
                    #     user.save()



                elif  data.validated_data['r_or_l']  == True or  data.validated_data['r_or_l']  == False and data.validated_data['places'] in [2,3]:
                    if amount_purchased(token_info.user.id) >= 20010000 and data.validated_data['places'] == 2:
                        data.save()
                        data.instance.user_id = token_info.user.id
                        data.instance.place = 2
                        data.instance.r_or_l = data.validated_data['r_or_l']
                        data.save()

                        mainU = MainUser.objects.filter(user_id=token_info.user.id).first()
                        mainU.payment_status = True
                        mainU.save()

                        main_check = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True).count()
                        if main_check == 1:
                            user = Users.objects.filter(id=data.validated_data['Owner'].id).first()
                            user.commission += 120000
                            user.save()



                    elif amount_purchased(token_info.user.id) >= 30015000 and data.validated_data['places'] == 3:
                        data.save()
                        data.instance.user_id = token_info.user.id
                        data.instance.place = 3
                        data.instance.r_or_l = data.validated_data['r_or_l']
                        data.save()

                        mainU = MainUser.objects.filter(user_id=token_info.user.id).first()
                        mainU.payment_status = True
                        mainU.save()

                        main_check = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True).count()
                        user = Users.objects.filter(id=data.validated_data['Owner'].id).first()
                        if main_check == 1:
                            user.commission += 120000
                            user.save()

                        def Anjam(id):
                            count = 2
                            check = Users.objects.filter(id=id).first()
                            main_user = MainUser.objects.filter(user_id=id).first()
                            user = Users.objects.filter(id=main_user.Owner.id).first()
                            if user.status == True:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                if count == 6:
                                    user.commission += 252000
                                    user.benـkala += 252000
                                    user.save()
                                else:
                                    user.commission += 504000
                                    user.save()
                            else: pass
                            main = MainUser.objects.filter(user_id=user.id).first()
                            if main is not None:
                                if count == 6:
                                    count -= 5
                                count+=1
                                Anjam(main.Owner.id)

                        mainR = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True,r_or_l=True).first()
                        mainL = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True,r_or_l=False).first()


                        if mainR.places == 3 and mainL.places == 3:
                            main_user = MainUser.objects.filter(user_id=mainR.Owner.id).first()
                            check = Users.objects.filter(id=mainR.Owner.id).first()
                            user = Users.objects.filter(id=main_user.user.id).first()

                            if user.status == True :
                                user = Users.objects.filter(id=main_user.user.id).first()
                                user.commission += 504000
                                user.save()
                            else: pass

                            main = MainUser.objects.filter(user_id=user.id).first()
                            if main is not None:
                                Anjam(main.user.id)

                    else:
                        return Response({'message': 'موجودی شما کافی نیست '})

                elif amount_purchased(token_info.user.id) >= 70035000 and data.validated_data['places'] == 7:
                    data.save()
                    data.instance.user_id = token_info.user.id
                    data.instance.places = 7
                    data.instance.r_or_l = data.validated_data['r_or_l']
                    data.save()
                    mainU = MainUser.objects.filter(user_id=token_info.user.id).first()
                    mainU.payment_status = True
                    mainU.save()

                    main_check = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True).count()
                    if main_check == 1:
                        user = Users.objects.filter(id=data.validated_data['Owner'].id).first()
                        user.commission +=  120000
                        user.save()

                    def Anjam(id):
                        count = 2
                        check = Users.objects.filter(id=id).first()
                        main_user = MainUser.objects.filter(user_id=id).first()
                        user = Users.objects.filter(id=main_user.Owner.id).first()
                        if user.status == True:
                            if count == 1:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += 504000
                                user.save()
                            elif count == 2:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += 504000 * 2
                                user.save()
                            elif count == 3:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += (504000 * 4) - 252000
                                user.benـkala += 252000
                                user.save()
                            elif count == 4:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += (504000 * 8) - 252000
                                user.benـkala += 252000
                                user.save()
                            elif count == 5:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += (504000 * 16) - 756000
                                user.benـkala += 756000
                                user.save()
                            elif count == 6:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += (504000 * 32)-1260000
                                user.benـkala += 1260000
                                user.save()


                        else:
                            pass

                        main = MainUser.objects.filter(user_id=user.id).first()
                        if main is not None:
                            if count == 7:
                                count -= 6
                            else: pass
                            count += 1
                            Anjam(main.Owner.id)


                    mainR = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id, payment_status=True,r_or_l=True).first()
                    mainL = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id, payment_status=True,r_or_l=False).first()

                    if mainR.places == 7 and mainL.places == 7:
                        main_user = MainUser.objects.filter(user_id=mainR.Owner.id).first()
                        check = Users.objects.filter(id=mainR.Owner.id).first()
                        user = Users.objects.filter(id=main_user.user.id).first()

                        if user.status == True:
                            user = Users.objects.filter(id=main_user.user.id).first()
                            user.commission += 504000
                            user.save()
                        else:
                            pass

                        main = MainUser.objects.filter(user_id=user.id).first()
                        if main is not None:
                            Anjam(main.user.id)


                else:
                    return Response({'message': 'موجودی شما کافی نیست '})
            else:

                # Rezerv

                if mainU is not None:
                    return Response({'message': 'کاربر قبلا  جایگاه انتخاب کرده است'})

                if owner_check is None:
                    return Response({'Owner': 'وجود ندارد'})
                else:
                    pass

                mainR = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id, payment_status=True,r_or_l=True).first()
                mainL = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id, payment_status=True,r_or_l=False).first()

                if mainR is not None and data.validated_data['r_or_l'] == True:
                    return Response({'message': 'راست کاربر پر است'})
                elif mainL is not None and data.validated_data['r_or_l'] == False:
                    return Response({'message': 'چپ کاربر پر است'})
                else:
                    pass

                mainU = MainUser.objects.filter(Owner_id=mainU_check.Owner.id).first()
                if data.validated_data['places'] == 1 and amount_purchased(token_info.user.id) >= 10005000:
                    mainU_check.payment_status = True
                    mainU_check.save()

                    #
                    # main_check = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id,payment_status=True).count()
                    # if main_check == 1:
                    #     user = Users.objects.filter(id=data.validated_data['Owner'].id).first()
                    #     user.commission += 120000
                    #     user.save()



                elif data.validated_data['r_or_l'] == True or data.validated_data['r_or_l'] == False and data.validated_data['places'] == 2:
                    if amount_purchased(token_info.user.id) >= 20010000 and data.validated_data['places'] == 2:
                        mainU_check.payment_status = True
                        mainU_check.save()



                        main_check = MainUser.objects.filter(Owner_id=mainU_check.Owner.id,payment_status=True).count()
                        if main_check == 1:
                            user = Users.objects.filter(id=mainU_check.Owner.id).first()
                            user.commission += 120000
                            user.save()



                    elif amount_purchased(token_info.user.id) >= 30015000 and data.validated_data['places'] == 3:
                        mainU_check.payment_status = True
                        mainU_check.save()



                        main_check = MainUser.objects.filter(Owner_id=mainU_check.Owner.id,payment_status=True).count()
                        user = Users.objects.filter(id=mainU_check.Owner.id).first()

                        if main_check == 1:
                            user.commission += 120000
                            user.save()

                        def Anjam(id):
                            count = 2
                            check = Users.objects.filter(id=id).first()
                            main_user = MainUser.objects.filter(user_id=id).first()
                            user = Users.objects.filter(id=main_user.Owner.id).first()
                            if user.status == True:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                if count == 6:
                                    user.commission += 252000
                                    user.benـkala += 252000
                                    user.save()
                                else:
                                    user.commission += 504000
                                    user.save()
                            else:
                                pass
                            main = MainUser.objects.filter(user_id=user.id).first()
                            if main is not None:
                                if count == 6:
                                    count -= 5
                                count += 1
                                Anjam(main.Owner.id)

                        mainR = MainUser.objects.filter(Owner_id=mainU_check.Owner.id, payment_status=True,r_or_l=True).first()
                        mainL = MainUser.objects.filter(Owner_id=mainU_check.Owner.id, payment_status=True,r_or_l=False).first()

                        if mainR.places == 3 and mainL.places == 3:
                            main_user = MainUser.objects.filter(user_id=mainR.Owner.id).first()
                            check = Users.objects.filter(id=mainR.Owner.id).first()
                            user = Users.objects.filter(id=main_user.user.id).first()

                            if user.status == True:
                                user = Users.objects.filter(id=main_user.user.id).first()
                                user.commission += 504000
                                user.save()
                            else:
                                pass

                            main = MainUser.objects.filter(user_id=user.id).first()
                            if main is not None:
                                Anjam(main.user.id)

                    else:
                        return Response({'message': 'موجودی شما کافی نیست '})

                elif amount_purchased(token_info.user.id) >= 70035000 and data.validated_data['places'] == 7:
                    mainU_check.payment_status = True
                    mainU_check.save()


                    main_check = MainUser.objects.filter(Owner_id=mainU_check.Owner.id,payment_status=True).count()
                    if main_check == 1:
                        user = Users.objects.filter(id=mainU_check.Owner.id).first()
                        user.commission += 120000
                        user.save()

                    def Anjam(id):
                        count = 2
                        check = Users.objects.filter(id=id).first()
                        main_user = MainUser.objects.filter(user_id=id).first()
                        user = Users.objects.filter(id=main_user.Owner.id).first()
                        if user.status == True:
                            if count == 1:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += 504000
                                user.save()
                            elif count == 2:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += 504000 * 2
                                user.save()
                            elif count == 3:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += (504000 * 4) - 252000
                                user.benـkala += 252000
                                user.save()
                            elif count == 4:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += (504000 * 8) - 252000
                                user.benـkala += 252000
                                user.save()
                            elif count == 5:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += (504000 * 16) - 756000
                                user.benـkala += 756000
                                user.save()
                            elif count == 6:
                                user = Users.objects.filter(id=main_user.Owner.id).first()
                                user.commission += (504000 * 32) - 1260000
                                user.benـkala += 1260000
                                user.save()


                        else:
                            pass

                        main = MainUser.objects.filter(user_id=user.id).first()
                        if main is not None:
                            if count == 7:
                                count -= 6
                            else:
                                pass
                            count += 1
                            Anjam(main.Owner.id)

                    mainR = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id, payment_status=True,r_or_l=True).first()
                    mainL = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id, payment_status=True,r_or_l=False).first()

                    if mainR.places == 7 and mainL.places == 7:
                        main_user = MainUser.objects.filter(user_id=mainR.Owner.id).first()
                        check = Users.objects.filter(id=mainR.Owner.id).first()
                        user = Users.objects.filter(id=main_user.user.id).first()

                        if user.status == True:
                            user = Users.objects.filter(id=main_user.user.id).first()
                            user.commission += 504000
                            user.save()
                        else:
                            pass

                        main = MainUser.objects.filter(user_id=user.id).first()
                        if main is not None:
                            Anjam(main.user.id)


                else:
                    return Response({'message': 'موجودی شما کافی نیست '})


            return Response({'message': 'جایگاه خریداری شد'})
        else:
            return Response({'message': 'Owner جایگاه خالی ندارد'})




class place_user_reservation(generics.CreateAPIView):
    serializer_class = MainUserSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = MainUserSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()

            user = Users.objects.filter(id=token_info.user.id).first()
            owner_check = MainUser.objects.filter(Owner_id=data.validated_data['Owner'].id).first()
            mainU = MainUser.objects.filter(user_id=token_info.user.id,payment_status=False).first()

            if mainU is not None:
                return Response({'message': 'کاربر قبلا  جایگاه انتخاب کرده است'})

            if owner_check is None:
                return Response({'Owner': 'وجود ندارد'})
            else: pass

            mainU = MainUser.objects.filter(Owner=data.validated_data['Owner'].id).first()
            if data.validated_data['places'] == 1:
                data.save()
                data.instance.place = 1
                data.instance.r_or_l = data.validated_data['r_or_l']
                data.save()



            elif  data.validated_data['r_or_l']  == True or  data.validated_data['r_or_l']  == False and data.validated_data['places'] in [2,3]:
                if data.validated_data['places'] == 2:
                    data.save()
                    data.instance.place = 2
                    data.instance.r_or_l = data.validated_data['r_or_l']
                    data.save()



                elif data.validated_data['places'] == 3:
                    data.save()
                    data.instance.place = 3
                    data.instance.r_or_l = data.validated_data['r_or_l']
                    data.save()

                else:
                    return Response({'message': 'موجودی شما کافی نیست '})

            elif data.validated_data['places'] == 7:
                data.save()
                data.instance.places = 7
                data.instance.r_or_l = data.validated_data['r_or_l']
                data.save()

            else:
                return Response({'message': 'موجودی شما کافی نیست '})



            # identifierـcode = "$" + "".join([choices(list(ascii_letters))[0] for _ in range(10)])
            # mainU_check = MainUser.objects.filter(identifierـcode=identifierـcode).first()
            # if mainU_check is not None:
            #     identifierـcode = "$" + "".join([choices(list(ascii_letters))[0] for _ in range(10)])
            # else: pass
            # data.instance.user_id = token_info.user.id
            # data.instance.identifierـcode = identifierـcode
            # data.save()
            mainU = MainUser.objects.filter(user_id=token_info.user.id).first()
            mainU.payment_status = False
            mainU.save()

            return Response({'message': 'جایگاه خریداری شد'})
        else:
            return Response({'message': 'Owner جایگاه خالی ندارد'})









class check_identifierـcode(generics.ListAPIView):
    serializer_class = MainUserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        identifierـcode = self.request.query_params.get('code',False)
        user = Users.objects.filter(identifierـcode=identifierـcode).first()
        if user is not None:
            return Response({'message': user.id})
        else:
            return Response({'message': 'کاربر وجود ندارد'})



class check_accses(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        contract = Contracts.objects.filter(user_id=token_info.user.id).first()
        card = Cards.objects.filter(user_id=token_info.user.id).first()
        user = Users.objects.filter(id=token_info.user.id).first()
        main_u = MainUser.objects.filter(user_id=token_info.user.id).first()

        if user.status == False:
            if contract is None:
                return Response({'message': 'خطا قرار داد فی ما برو تایید کنید'},status=status.HTTP_400_BAD_REQUEST)
            elif card is None:
                return Response({'message': 'خطا  اطلاعات حساب را اضافه  کنید'},status=status.HTTP_400_BAD_REQUEST)
            elif user.Book_or_buy_goods != True:
                return Response({'message': 'خطا  امتیاز خود  را انتخاب  کنید'}, status=status.HTTP_400_BAD_REQUEST)
            elif main_u is None:
                return Response({'message': 'خطا  جایگاه خود را انتخاب  کنید'},status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({'message': 'حساب کاربر فعال شد'})

        else:
            return Response({'message': 'حساب کاربر فعال است'})




class select_points(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = SelectPointsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            user = Users.objects.filter(id=token_info.user.id).first()
            user.Book_or_buy_goods = data.validated_data['Book_or_buy_goods']
            user.save()
            return Response({'message': 'بروزرسانی شد'})

        else:
            return Response(data.errors)




class sub_categories_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        main_u = MainUser.objects.filter(Owner_id=token_info.user.id).count()
        return Response({'number': main_u})




class place_active_right_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user = Users.objects.filter(id=id).frist()
        r_user = MainUser.objects.filter(Owner_id=user.id,payment_status=True,main__r_or_l=True).count()
        return Response({'number': r_user})



class place_active_left_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user = Users.objects.filter(id=id).frist()
        l_user = MainUser.objects.filter(Owner=user.id,payment_status=True,main__r_or_l=False).count()
        return Response({'number': l_user})



class place_reservation_right_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user = Users.objects.filter(id=id).frist()
        r_user = MainUser.objects.filter(Owner_id=user.id,payment_status=False,main__r_or_l=True).count()
        return Response({'number': r_user})



class place_reservation_left_number(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user = Users.objects.filter(id=id).frist()
        l_user = MainUser.objects.filter(Owner_id=user.id,payment_status=False,main__r_or_l=False).count()
        return Response({'number': l_user})


class orders_list(generics.ListAPIView):
    serializer_class = DerakhtiOrdersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProductsOrders.objects.filter(shopper_id=token_info.user.id, payment_status=True).all().order_by('id')


class places_list(generics.ListAPIView):
    serializer_class = MainUserSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        places = MainUser.objects.filter(Owner_id=token_info.user.id, payment_status=True).all()
        main = MainUser.objects.filter(user_id=token_info.user.id, payment_status=True).first()
        if main:
            result = []
            result.append({'main': {'Owner': main.Owner.username,'user': main.user.username,'places': main.places,'r_or_l': main.r_or_l,'payment_status': main.payment_status }})
            count = 0
            for p in places:
                result.append({'Owner': p.Owner.username,'user': p.user.username,'places': p.places,'r_or_l': p.r_or_l,'payment_status': p.payment_status})
                count += 1

            if count != 15:
                while count < 15:
                    result.append({'Owner': None,'user': None,'places': None,'r_or_l': None,'payment_status': None})
                    count += 1

            return Response(result)
        else:
            return Response({'result': None})



class places_list_filter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        username = self.request.query_params.get('username',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        places = MainUser.objects.filter(Owner__username=username, payment_status=True).all()
        main = MainUser.objects.filter(user__username=username, payment_status=True).first()
        if main:
            result = []
            result.append({'main': {'Owner': main.Owner.username,'user': main.user.username,'places': main.places,'r_or_l': main.r_or_l,'payment_status': main.payment_status}})
            count = 0
            for p in places:
                result.append({'Owner': p.Owner.username,'user': p.user.username,'places': p.places,'r_or_l': p.r_or_l,'payment_status': p.payment_status})
                count += 1

            return Response(result)
        else:
            return Response({'result': None})






class user_info(generics.ListAPIView):
    serializer_class = UsersSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        user = Users.objects.filter(id=token_info.user.id).first()
        card = Cards.objects.filter(user_id=token_info.user.id).first()
        walletـbalance  = [ p.price_drsd for p in DerakhtiProductsOrders.objects.filter(payment_status=True,shopper_id=token_info.user.id).all()]
        if card is not None:
            return Response({'info': {'first_name': card.first_name,'last_name': card.last_name,'accountـnumber': card.accountـnumber,'shaba_number': card.shaba_number,'user_status': user.status,'mobile1': user.mobile1,'vocher': user.benـkala,'porsant': user.commission,'status': user.status}})
        else:
            return Response({'info': 'empty'})




class deposit_request(generics.ListAPIView):
    serializer_class = DepositRequestSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        price = self.request.query_params.get('price',False)
        if price or price < 1:
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            user = Users.objects.filter(id=token_info.user.id).first()

            depositrequest = DepositRequest.objects.filter(user_id=user.id,status=True).first()
            if depositrequest is not None:

                date_now = str(depositrequest.date).split(' ')[0].replace('-', ',')
                date_spilt = date_now.split(',')
                date = datetime.date(int(date_spilt[0]), int(date_spilt[1]), int(date_spilt[2]))
                x = datetime.timedelta(7)
                haft = str(date - x).split('-')
                haft2 = datetime.date(int(haft[0]), int(haft[1]), int(haft[2]))

                if haft2 < date:
                    user.commission -= int(price)
                    user.save()
                    dp = DepositRequest.objects.create(user_id=user.id, price=price)
                    return Response({'message': 'درخواست واریز ثبت شد'})

            else:
                depositrequest = DepositRequest.objects.filter(user_id=user.id, status=False).first()
                if depositrequest is None:
                    user.commission -= int(price)
                    user.save()
                    dp = DepositRequest.objects.create(user_id=user.id, price=price)
                    return Response({'message': 'درخواست واریز ثبت شد'})
                else:
                    return Response({'message': 'قبلا درخواست دادید'})

        else:
            return Response({'price': 'وارد نشده'})


class product_canel(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        product = DerakhtiProductsOrders.objects.filter(shopper_id=token_info.user.id,product_id=id,payment_status=True).first()
        if product is not None:
            date_now = str(product.payment_date).split(' ')[0].replace('-', ',')
            date_spilt = date_now.split(',')
            date = datetime.date(int(date_spilt[0]), int(date_spilt[1]), int(date_spilt[2]))
            x = datetime.timedelta(7)
            haft = str(date - x).split('-')
            haft2 = datetime.date(int(haft[0]),int(haft[1]),int(haft[2]))


            date_now = str(product.payment_date).split(' ')[0].replace('-', ',')
            date_spilt = date_now.split(',')
            date = datetime.date(int(date_spilt[0]), int(date_spilt[1]), int(date_spilt[2]))
            x = datetime.timedelta(180)
            mah = str(date - x).split('-')
            mah2 = datetime.date(int(haft[0]),int(haft[1]),int(haft[2]))

            user = Users.objects.filter(id=token_info.user.id).first()



            if haft2 < date:
                cancel = CanelProduct.objects.create(user_id=product.shopper.id,product_id=product.id,price=product.price_drsd,mobile1=product.shopper.mobile1,mobile2=product.shopper.mobile2)
                product.delete()
                return Response({'message': 'درخواست کنسلی ثبت شد'})

            elif mah2 < date:
                cancel = CanelProduct.objects.create(user_id=product.shopper.id,product_id=product.id,price=product.price_drsd,mobile1=product.shopper.mobile1,mobile2=product.shopper.mobile2)
                product.delete()
                return Response({'message': 'درخواست کنسلی ثبت شد'})
            else:
                return Response({'message': 'نمیتونید کنسل کنید باید ۶ ماه بگذره'})
        else:
            return Response({'message': 'موجود نیست'})






class admin_products_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProducts.objects.filter(user_id=token_info.user.id,status=True).all()


class admin_main_categories(generics.ListAPIView):
    serializer_class = DerakhtiProductMainCategoriesSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProductMainCategories.objects.all()


class admin_sub_categories1(generics.ListAPIView):
    serializer_class = DerakhtiProductSubCategories_1Serializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        sub_categories1 = DerakhtiProductSubCategories_1.objects.filter(products__maincategories__id=id).distinct()

        return Response({'info': [{s1.id:s1.name}  for s1 in sub_categories1] })


class admin_sub_categories2(generics.ListAPIView):
    serializer_class = DerakhtiProductSubCategories_2Serializers
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        sub_categories2 = DerakhtiProductSubCategories_2.objects.filter(products__subCategories1__id=id).distinct()
        return Response({'info': [{s2.id:s2.name}  for s2 in sub_categories2] })



class admin_products_purchased(generics.ListAPIView):
    serializer_class = DerakhtiOrdersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProductsOrders.objects.filter(product__user__id=token_info.user.id,payment_status=True).all()


class admin_products_comments_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsCommentsSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        return DerakhtiProductsComments.objects.filter(product__user__id=token_info.user.id).all()


class admin_products_add(generics.CreateAPIView):
    serializer_class = DerakhtiProductsSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = DerakhtiProductsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            data.save()
            data.instance.user = token_info.user
            data.save()

            return Response({'message': 'با موفقیت اضافه شد'})
        else:
            return Response(data.errors)


class admin_products_update(generics.UpdateAPIView):
    serializer_class = DerakhtiProductsUpdateSerializers
    permission_classes = [IsAuthenticated]


    def update(self, request, *args, **kwargs):
        data = DerakhtiProductsUpdateSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            product = DerakhtiProducts.objects.filter(id=data.validated_data['id'],user_id=token_info.user.id).first()
            if product is not None:
                data.update(product,data.validated_data)
                return Response({'message': 'با موفقیت بروز شد'})
            else:
                return Response({'message': 'وجود ندارد'})
        else:
            return Response(data.errors)


class admin_products_delete(generics.CreateAPIView):
    serializer_class = DerakhtiProductsSerializers
    permission_classes = [IsAuthenticated]


    def post(self,request):
        id = self.request.query_params.get('id',False)
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        product = DerakhtiProducts.objects.filter(id=id,user_id=token_info.user.id).first()
        if product is not None:
            product.delete()
            return Response({'message': 'حذف شد'})
        else:
            return Response({'message': 'وجود ندارد'},status=status.HTTP_400_BAD_REQUEST)



class carts_add(generics.CreateAPIView):
    serializer_class = DerakhtiOrdersSerializers

    def post(self, request, *args, **kwargs):
        data = DerakhtiOrdersSerializers(data=request.data)
        if data.is_valid():
            user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            cart = DerakhtiProductsCarts.objects.filter(user_id=token_info.user.id).first()
            if cart is None:
                cart_create = DerakhtiProductsCarts.objects.create(user_id=token_info.user.id)
            else: pass
            cart = DerakhtiProductsCarts.objects.filter(user_id=token_info.user.id).first()
            product = DerakhtiProducts.objects.filter(id=data.validated_data['product'].id).first()
            DerakhtiProductsOrders.objects.create(shopper_id=token_info.user.id,title=product.title,description=product.descriptions,price=product.price,cart_id=cart.id,product_id=product.id)
            return Response({'message': 'اضافه شد'})
        else:
            return Response(data.errors)

class carts_remove(generics.CreateAPIView):
    serializer_class = DerakhtiOrdersSerializers


    def post(self, request, *args, **kwargs):
        data = DerakhtiOrdersSerializers(data=request.data)
        if data.is_valid():
            id = request.data.get('id',False)
            if id:
                user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
                token_info = Token.objects.filter(key=user_token).first()
                cart = DerakhtiProductsCarts.objects.filter(user_id=token_info.user.id).first()
                order = DerakhtiProductsOrders.objects.filter(id=id,product_id=data.validated_data['product'].id,payment_status=False).first()
                if order is not None:
                    order.delete()
                    return Response({'message': 'حذف شد'})
                else:
                    return Response({'message': 'error'})
            else:
                return Response({'id': 'این فیلد الزامی است'})
        else:
            return Response(data.errors)




class carts_list(generics.ListAPIView):
    serializer_class = DerakhtiOrdersSerializers

    def get_queryset(self):
        user_token = str(self.request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        cart = get_object_or_404(DerakhtiProductsCarts,user_id=token_info.user.id)
        return DerakhtiProductsOrders.objects.filter(cart_id=cart.id,payment_status=False).all().order_by('id')




class products_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsSerializers

    def get_queryset(self):
        return DerakhtiProducts.objects.filter(status=True,vocher=False).all()

class products_list_vocher(generics.ListAPIView):
    serializer_class = DerakhtiProductsSerializers

    def get_queryset(self):
        return DerakhtiProducts.objects.filter(status=True,vocher=True).all()


class products_comments_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsCommentsSerializers

    def get_queryset(self):
        product_id = self.request.query_params.get('id',False)
        return DerakhtiProductsComments.objects.filter(product_id=product_id,status=True).all()




class products_comments_add(generics.CreateAPIView):
    serializer_class = DerakhtiProductsCommentsSerializers
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = DerakhtiProductsCommentsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            productComments_check = DerakhtiProductsComments.objects.filter(user_id=token_info.user.id,product_id=data.validated_data['product'].id,status=False).first()
            if productComments_check is None:
                DerakhtiProductsComments(user_id=token_info.user.id, product_id=data.validated_data['product'].id,comment=data.validated_data['comment'], status=False).save()
                return Response({'message': 'دیدگاه ثبت شد'})
            else:
                return Response({"message": "کاربر قبلا برای این محصول دیدگاه ثبت کرده است"})
        else:
            return Response(data.errors)


class products_filter_maincategory_list(generics.ListAPIView):
    serializer_class = DerakhtiProductsSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id',False)
        return DerakhtiProducts.objects.filter(maincategories__id=id,status=True).all()

