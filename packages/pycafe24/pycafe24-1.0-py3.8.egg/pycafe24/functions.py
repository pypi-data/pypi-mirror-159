import requests
import json
from .exceptions import Cafe24Exception

class Cafe24Client(object):
	def __init__(self,credentials_manager):
		self.credentials_manager = credentials_manager




	def _post(self,url,payload):
		headers = {
					'Authorization': "Bearer {0}".format(self.credentials_manager.access_token),
					'Content-Type': "application/json",
					'X-Cafe24-Api-Version': "2022-06-01",
					'X-Api-Call-Limit': "1/40"
					}
		print(payload)
		print(headers)
		print(url)
		response = requests.request("POST",url,data=payload,headers=headers)
		return response

	def _get(self,url,payload):
		headers = {
					'Authorization': "Bearer {0}".format(self.credentials_manager.access_token),
					'Content-Type': "application/json",
					'X-Cafe24-Api-Version': "2022-06-01",
					'X-Api-Call-Limit': "1/40"
					}
		print(payload)
		print(headers)
		print(url)
		response = requests.request("POST",url,data=payload,headers=headers)
		return response




	def create_coupon(self,
					coupon_name,
					benefit_type,
					issue_type,
					available_period_type,
					available_begin_datetime,
					available_end_datetime,
					available_day_from_issued,
					available_site,
					available_scope,
					available_product,
					available_product_list,
					available_category,
					available_category_list,
					available_amount_type,
					available_coupon_count_by_order,
					available_price_type,
					available_order_price_type,
					available_in_price,
					discount_amount,
					discount_rate):

		"""
		Creates a coupon

		Parameters:
			Required
				- coupon_name : name of coupon
				- benefit_type : benefit type (A: flat discount, B: percentage discount)
				- issue_type : issue type of coupon (M)
				- available_period_type : available date type of coupon (F: general period, R: dependent on coupon issuance date, M: until end of current month)
				- available_site : available site (W: web only, M: mobile only, use both W and M for web and mobile)
				- available_scope : available scope (P: coupon available only for product, O: coupon available for order)
				- available_product : products that the following coupon can use (U: no restrictions, I: apply only products listed in available_product_list, E: exclude products listed in available_product_list)
				- available_category : categories that the following coupon can use (U: no restrictions, I: apply only categories listed in available_product_list, E: exclude products listed in available_product_list)
				- available_amount_type : When the coupon can be applied (E: before payment discount, I: after payment discount)
				- available_coupon_count_by_order : Max number of coupon that can be used per order
		"""

		url = "https://{0}.cafe24api.com/api/v2/admin/coupons".format(self.credentials_manager.mall_id)

		payload = {
			"request": {
				"coupon_name": coupon_name,
				"benefit_type": "A",
				"issue_type": "M",
				"available_period_type": "M",
				"available_site": ["W","M"],
				"available_scope": "O",
				"available_product": "U",
				"available_category": "U",
				"available_amount_type": "E",
				"available_coupon_count_by_order": 1,
				"discount_amount": {
					"benefit_price": "10000"
				}
			}
		}

		response = self._post(url,payload=json.dumps(payload))
		return response


	def issue_coupon(self,
					coupon_no,
					issued_member_scope,
					group_no,
					member_id,
					send_sms_for_issue,
					allow_duplication,
					single_issue_per_once,
					issue_count_per_once,
					issued_place_type,
					issued_by_action_type,
					issued_by_event_type,
					request_admin_id):
		pass


	def retrieve_points(self,member_id,email,order_id,group_no,start_date,end_date,case,points_category,offset,limit):

		pass

	def modify_points(self,member_id, amount, type, **rest):
		payload = {}
		request = {}

		url = "https://{0}.cafe24api.com/api/v2/admin/points".format(self.credentials_manager.mall_id)


		if len(member_id) > 20 and len(member_id) <= 0:
			raise Cafe24Exception(-1,-1,"member_id has to be between 0 ~ 20 characters")
		request["member_id"] = member_id

		if float(amount) <= 0 and float(amount) > 1000000:
			raise Cafe24Exception(-1,-1,"amount has to be between 0 ~ 1,000,000")
		request["amount"] = amount


		if not (type == "increase" or type == "decrease"):
			raise Cafe24Exception(-1,-1,"point type has to be either 'increase' or 'decrease'")
		request["type"] = type

		for (key,value) in rest.items():
			if key == "shop_no":
				payload[key] = value
			else:
				request[key] = value

		payload["request"] = request

		response = self._post(url,payload=json.dumps(payload))
		return response
