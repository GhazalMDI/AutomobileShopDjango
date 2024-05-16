from django.db import models
from django.urls import reverse

from utils.baseModel import BaseModel
from ckeditor.fields import RichTextField



class Product(BaseModel):
    image = models.ImageField(upload_to='products/%Y/%M/%d',null=True,blank=True)
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField(null=True,blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=255)
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True, blank=True)
    available = models.BooleanField(default=True,null=True)
    categoryOne = models.ForeignKey('Category_one', models.SET_NULL, 'categoryOneProduct', null=True)
    categoryTwo = models.ForeignKey('Category_two', models.SET_NULL, 'categoryTwoProduct', null=True)
    description = RichTextField(null=True,blank=True)
    brand = models.ForeignKey('Brand',models.SET_NULL,'productBrand',null=True,blank=True)
    # attrs = models.ManyToManyField('AttributeValue')
    def __str__(self):
        return f'{self.name}-{self.unit_price}'

    @property
    def after_discount(self):
        if self.discount:
            self.unit_price = (100 - self.discount) * self.unit_price // 100
            return self.unit_price
        return self.unit_price

    @property
    def get_absolute_url(self):
        return reverse('products:productDetails',args=(self.slug,self.id))

class Brand(BaseModel):
    name = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255,null=True)
    def __str__(self):
        return f'{self.name}-{self.englishName}'


class Comment(BaseModel):
    user = models.ForeignKey('accounts.User',models.CASCADE,'comment_user')
    product = models.ForeignKey('Product',models.CASCADE,'product_comment')
    replay_to = models.ForeignKey('self',models.CASCADE,'comment_replay',null=True,blank=True)
    active = models.BooleanField(default=False)
    is_replay = models.BooleanField(default=False)
    body = RichTextField()

    def __str__(self):
        return f'{self.user.phone_number}-{self.product.name}'
    #
    # def __len__(self):
    #     return len(Comment.objects.filter(active=True))
class Category_one(BaseModel):
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(unique=True, allow_unicode=True, null=True)

    def __str__(self):
        return self.name


class Category_two(BaseModel):
    catagoryOne = models.ForeignKey('Category_one', models.CASCADE, 'sub_cat_two')
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(unique=True, allow_unicode=True, null=True)


    def __str__(self):
        return self.name


class Like(models.Model):
    product = models.ForeignKey('Product',models.SET_NULL,null=True,blank=True,related_name='product_like')
    user = models.ForeignKey('accounts.User',models.CASCADE,blank=True,null=True,related_name='user_like')
    def __str__(self):
        return f'{self.product.name}-{self.user.phone_number}'


class GalleryProduct(models.Model):
    image = models.ImageField(upload_to='galleryProduct/%y/%M/%d',null=True,blank=True)
    imageGallery = models.ForeignKey('Product',models.SET_NULL,'galleryProduct',null=True)
#
