from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class Post_Manger(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    #? 🚀 comment manage functions 🚀
    def comments_of_post(self , post_id ,titel ,  time_pub):
        #porbleme here that can uer send a id of the other postes and show up thier comments
        post = self.get_queryset().get(id = post_id , titel = titel , time_pub = time_pub)

        return Comment.objects.filter(post_comment = post)
    
    def comment_a_post(self):
        pass #$ we make it in the viwes by usning the serializer

    def update_comment(self):
        pass #$ we make it in the viwes by usning the serializer
    
    def delete_comment(self, comment_id , ownerComment_id , post_id):  
        Comment.objects.get(id = comment_id , user_comment = ownerComment_id , post_comment = post_id).delete()
 
    #? 🚀 User  manages functions 🚀
    def owner_post(self , post_id ,titel ,  time_pub):
        target_post = self.get_queryset().get(id = post_id , titel = titel , time_pub = time_pub)
        record = Post_Owner.objects.get( post_of_owner = target_post)
        return record.owner
    
    def persones_commented(self , post_id ,titel ,  time_pub) : 
        target_post = self.get_queryset().get(id = post_id , titel = titel , time_pub = time_pub)
        persones_commented = Comment.objects.filter(post_comment = target_post)
        # * retruent a list of user that commented this post
        persons  = list()
        for usr in persones_commented : 
            persons.append(usr.user_comment)

        return persons
    
    #? 🚀 post functions 🚀
    def create_post_owner (self , owner_id , post_id):
        post_id = self.get_queryset().get  (    id = post_id.get('id') ,
                                                time_pub = post_id.get('time_pub')
                                            )
        owner_id = User.objects.get (   id = int(owner_id.get('id')) ,
                                        username = owner_id.get('user_name') , 
                                        date_joined = owner_id.get('date_joined')
                                    )
        
        Post_Owner.objects.create( owner = owner_id , post_of_owner = post_id)


    def post_delete(self , post_id  ,titel ,  time_pub):
        #? if we deleete a post than the owner record deleted and the commentes related to this post deleted
        target_post = self.get_queryset().get(id = post_id , titel = titel , time_pub = time_pub)
        try:
            Post_Owner.objects.get(post_of_owner = target_post).delete()
        except : 
            pass
       
        if Comment.objects.filter(post_comment = target_post).exists():
            Comment.objects.filter(post_comment = target_post).delete()

       
        #? than delete the post 
        target_post.delete()

    def get_postes   (self , user,num_recommendations = 8) : #$  postes recommendated by titel
        user = User.objects.get(id = user) 

        #$ take all the titel post of the current user
        post_user = Post_Owner.objects.filter( owner = user)
        user_postes = [ _.post_of_owner for _ in post_user]
        list_usr_post_title = [_.titel for _ in user_postes]
        id_postes_user = [_.id for _ in user_postes]

        #$ postes titles that the current user is commented
        user_post_commented = Comment.objects.filter( user_comment = user)
        user_commented_on = [_.post_comment for _ in user_post_commented]
        titel_posted_commented = [_.titel for _ in user_commented_on]
        id_aredy = [_.id for _ in user_commented_on] #* postes that aredy commented so aredy wach it so we don't need to recommend it



        #* and then filter all the postes that have the simlir titel
        recommendaed_postes = self.get_queryset().filter( 
                Q(titel__in = list_usr_post_title) | Q(titel__in = titel_posted_commented)
            ).exclude(
                Q(id__in = id_postes_user) | Q(id__in = id_aredy)
            ).order_by('?')
        

        return recommendaed_postes[:num_recommendations]

        


        

    







    

class Post(models.Model):
    titel = models.CharField(null=False , blank= False , max_length=20)
    time_pub = models.TimeField(auto_now = False , auto_now_add = True)
    #$data = models.DateField(auto_now = False , auto_now_add = True )
    text = models.TextField(default="None")
    postes = Post_Manger()

    def __str__(self) -> str:
        return super().__str__()


class Comment(models.Model):
    user_comment = models.ForeignKey(User , on_delete= models.CASCADE)
    post_comment = models.ForeignKey(Post , on_delete= models.CASCADE)
    text = models.TextField(default="None")
    #$data = models.DateField(auto_now = False , auto_now_add = True )
    #modify this table append to it a date filed 


class Post_Owner(models.Model):
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    post_of_owner = models.OneToOneField(Post , on_delete= models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()



