x=input("Enter no of shoes")
sizes= [2,3,4,5,7,6,9,8,10]
n= input("no of customers")
d={}
c=100
for i in sizes:
    d[i]= c
    c = c+100
    d.update(d)
print(d)
    
    from django.contrib.auth import get_user_model
    user = get_user_model().objects.get(id=2184)
    https://carl-qa.herokuapp.com
    
    287--banking


                        
                        
                    # if 'new_phone_number' in meta:
                        # phone_number = meta.pop('new_phone_number')
                        # user = User.objects.get(phone_number = phone_number)
                        # user_linked = UserLinkedAccounts.objects.filter(user=user, active=True)
                        # if user_linked:
                        #     if user.last_modified_at > (timezone.now() - relativedelta(days=30)):
                        #         send_new_otp(user, meta) 
                        
                        
USER save method
def save(self, *args, **kwargs):
        if self.email == "" or self.email is None:
            self.email = None
        self.total_cash = self.investment_cash \
            + self.available_cash \
            + self.unavailable_cash
        
        UserEmails.objects.update_or_create(
            user= self.user,
            email= self.email,
            updated_on = timezone.now)

        super(User, self).save(*args, **kwargs)


class UserEmails(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField(max_length=70, null=True, unique=True, default=None)
    updated_on = models.DateTimeField(null=False, default=timezone.now)

    class Meta:
        db_table = 'carl_user_emails'
        verbose_name = 'CARL User Emails'
    
    def get_email_list(self, *args, **kwargs):
        email_list = []
        user= User.objects.filter(user=self.user)
        email_list.append(user.email)
        return email_list

# class UserEmails(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     email = models.JSONField(default=list)
#     updated_on = models.DateTimeField(null=False, default=timezone.now)

#     class Meta:
#         db_table = 'carl_user_emails'
#         verbose_name = 'CARL User Emails'

#     def save(self, *args, **kwargs):
#         self.email = self.email.lower().strip()
#         if self.email != "":
#             if not email_re.match(self.email):
#                 raise ValidationError(u'%s is not a valid email address, Please enter valid email-address' % self.email)
#         super(UserEmails, self).save(*args, *kwargs)

----------------------carl.views.py------------
update:

user.meta = json.dumps(meta)
user.save()
user.refresh_from_db()
# new_email = request_data.get('email')
# user_email = UserEmails.objects.filter(user=user).update(email= new_email )
# user_email.refresh_from_db()
        
add:

user.meta = json.dumps(meta)
                user.save()
                user.refresh_from_db()
                # new_email = request_data.get('email')
                # user_emai = UserEmails.objects.create( user = user, email = new_email)
                
--------------serializers.py------------
# class UserEmailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserEmail
#         fields = ('id','email', 'updated_on')


