import random

from locust import HttpUser, task, between, TaskSet

products = {
    'Sunglasses': 'OLJCESPC7Z',
    'Tank Top': '66VCHSJNUP',
    'Watch': '1YMWWN1N4O',
    'Loafers': 'L9ECAV7KIM',
    'Hairdryer': '2ZYFJ3GM2N',
    'Candle Holder': '0PUK6V6EV0',
    'Salt & Pepper Shakers': 'LS4PSXUNUM',
    'Bamboo Glass Jar': '9SIQT8TOJO',
    'Mug': '6E92ZMYYFZ',
    'Playstation': '56FGN9KLSN',
    'Football': 'FACYUJE34M'
}

currencies = [
    'USD',
    'EUR',
    'JYP',
    'GBP',
    'TRY',
    'CAD'
]


class WebTest(TaskSet):

    def on_start(self):
        self.client.get('/', name=self.on_start.__name__)
        print('Start')

    @task(3)
    def browse_products(self):
        random_item = random.choice(list(products.items()))
        random_key, random_value = random_item
        url = '/product/' + random_value
        print(f'Opening {random_key} page')
        self.client.get(url, name=self.browse_products.__name__)

    @task(1)
    def browse_cart(self):
        print('Opening Cart')
        self.client.get('/cart', name=self.browse_cart.__name__)

    @task(3)
    def add_product(self):
        random_item = random.choice(list(products.items()))
        random_key, random_value = random_item
        print(f'Adding {random_key} to cart')
        self.client.post('/cart', data=f'''product_id={random_value}&quantity=1''', name=self.add_product.__name__)

    @task(1)
    def empty_cart(self):
        print('Emptying Cart')
        self.client.post('cart/empty', name=self.empty_cart.__name__)

    @task(2)
    def change_currencies(self):
        ran_cur = random.choice(currencies)
        print(f'Changing currencies to {ran_cur}')
        self.client.post('setCurrency', data=f'''currency_code={ran_cur}''', name=self.change_currencies.__name__)

    @task(1)
    def checkout_cart(self):
        print(f'Checking out cart')
        self.client.post('cart/checkout', data='''email=someone%40example.com&street_address=1600+Amphitheatre
        +Parkway&zip_code=94043&city=Mountain+View&state=CA&country=United+States&credit_card_number=4432-8015
        -61520454 &credit_card_expiration_month=1&credit_card_expiration_year=2024&credit_card_cvv=672''',
                         name=self.checkout_cart.__name__)

    def on_stop(self):
        self.client.get('', name=self.on_stop().__name__)
        print('Stop')


class MyUser(HttpUser):
    host = 'https://onlineboutique.dev/'
    wait_time = between(.5, 3)
    tasks = [WebTest]
