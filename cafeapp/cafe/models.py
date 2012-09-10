# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

import datetime


class Product(models.Model):
	name = models.CharField(max_length = 30)
	price = models.FloatField()
	
	amount = models.FloatField(blank = True)
	selled_amount = models.FloatField(blank=True)
	
	available = models.BooleanField(default = True)
	
	def __unicode__(self):
		return u"%s: %s,- kč" % (self.name, self.price)
	
	class Meta:
		ordering = ["-available",'name']



class SubOrder(models.Model):
	"""
	This is model for single order
	it should be used later in complex order
	"""
	
	product = models.ForeignKey(Product)
	quantity = models.SmallIntegerField()
	
	def __unicode__(self):
		if self.quantity > 1:
			return "%s*%s" % (self.quantity, self.product.name)
		else:
			return self.product.name

@receiver(post_save, sender=SubOrder, dispatch_uid="new_suborder")
def sub_order_handler(sender, instance, **kwargs):
	"If the new suborder is created then we have to decrease the amount of product"
	instance.product.amount -= instance.product.selled_amount * float(instance.quantity) 
	instance.product.save() 





class Order(models.Model):
	"""Model for complex order containing many SubOrder instances"""
	
	customer = models.CharField(max_length = 20)
	day = models.DateTimeField(auto_now = True)
	paid  = models.BooleanField(default = False)

	sub_orders = models.ManyToManyField(SubOrder)

	selled_by = models.ForeignKey(User)   

	class Meta:
		ordering = ['-day']
		
			
	def products(self):
		sub_orders_in_string = map(lambda x: x.__unicode__(), self.sub_orders.all())
		return ", ".join(sub_orders_in_string)
	
	
	def price(self):
		money_spent = 0
		for order in self.sub_orders.all():
			money_spent += order.product.price * order.quantity		
			
		return money_spent
			
	def __unicode__(self):
		paid = "zaplaceno" if self.paid else "dluzi"
		return u"%s: %s utratil: %s,- kč, Stav: %s" % (self.day, self.customer, self.price(), paid)   
	

class CashboxState(models.Model):
	day_of_the_counting = models.DateTimeField(auto_now_add=True)
	money = models.IntegerField()
	predicted_result = models.IntegerField()
	accounted_by = models.ForeignKey(User)
	
	
	positive = predicted_result < money # this will be used later 
	
	def __unicode__(self):
		return u"%s: %s,- kč" % (self.day_of_the_counting, self.money)  
	
	class Meta:
		ordering = ['-day_of_the_counting']
	
	# ---- static methods used to determine how much should be in cashbox:
	
	@staticmethod
	def get_yestedays_money():
		if len(CashboxState.objects.all())>0: # if there was some cashbox state:
			yesterdays_money = CashboxState.objects.latest("day_of_the_counting")
		else:
			yesterdays_money = False # we dont use NoneType cause it cant be expressed as number
		return yesterdays_money

	@staticmethod
	def get_profit():
		yesterdays_money = CashboxState.get_yestedays_money()
		if yesterdays_money:
			min_date = yesterdays_money.day_of_the_counting
			
			latest_orders = Order.objects.filter(paid = True, day__gt=min_date)
		else: # if there was no cash written
			latest_orders = Order.objects.filter(paid = True)
		
		return sum( [order.price() for order in latest_orders])
	
	@staticmethod
	def get_expanses():
		yesterdays_money = CashboxState.get_yestedays_money()
		if yesterdays_money:			
			latest_expanses = Expanse.objects.filter(time__range = (
							 yesterdays_money.day_of_the_counting,
							 datetime.datetime.now() ))
			
		else: # if there was no cash written
			#latest_orders = Order.objects.filter(day__startswith = datetime.datetime.today().date(), paid = True)
			latest_expanses = Expanse.objects.all()
			
		return sum( [expanse.money for expanse in latest_expanses])
		
	@staticmethod
	def predict_result():		
		yesterdays_money = CashboxState.get_yestedays_money()
		profit = CashboxState.get_profit()
		expanses = CashboxState.get_expanses()
		# profit + yesterdays money if any.
		predicted_result = profit + yesterdays_money.money if yesterdays_money else profit
		predicted_result -= expanses
		
		return predicted_result
	

class Expanse(models.Model):
	money = models.PositiveIntegerField()
	description = models.TextField()
	user = models.ForeignKey(User)
	time = models.DateTimeField(default=datetime.datetime.now())

	def __unicode__(self):
		return "%s : %s" % (self.description, self.money)
	
	class Meta:
		ordering = ['-time']
	


	
