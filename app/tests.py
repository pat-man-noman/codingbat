from django.test import TestCase

# Create your tests here.
class TestWarmup1(TestCase):
    def test_warmup_1_93(self):
        response =self.client.get('/warmup1/near-hundred/93')
        self.assertContains(response, True)

    def test_warmup_1_90(self):
        response =self.client.get('/warmup1/near-hundred/90')
        self.assertContains(response, True)
    
    def test_warmup_1_89(self):
        response =self.client.get('/warmup1/near-hundred/89')
        self.assertContains(response, False)
class TestWarmup2(TestCase):
    def test_warmup_2_code(self):
        response =self.client.get('/warmup2/String-Splosion/Code')
        self.assertContains(response, "CCoCodCode")
    def test_warmup_2_abc(self):
        response =self.client.get('/warmup2/String-Splosion/abc')
        self.assertContains(response, "aababc")
    def test_warmup_2_ab(self):
        response =self.client.get('/warmup2/String-Splosion/ab')
        self.assertContains(response, "aab")
class TestString(TestCase):
    def test_String2_catdog(self):
        response =self.client.get('/string2/cat-dog/catdog')
        self.assertContains(response, True)

    def test_String2_catcat(self):
        response =self.client.get('/string2/cat-dog/catcat')
        self.assertContains(response, False)

    def test_String2_1cat1cadodog(self):
        response =self.client.get('/string2/cat-dog/1cat1cadodog')
        self.assertContains(response, True)
class TestLogic(TestCase):
    def test_Logic2_6(self):
        response =self.client.get("/Logic2/lone-sum/1/2/3")
        self.assertContains(response, 6)
    def test_Logic2_2(self):
        response =self.client.get("/Logic2/lone-sum/3/2/3")
        self.assertContains(response, 2)
    def test_Logic2_0(self):
        response =self.client.get("/Logic2/lone-sum/3/3/3")
        self.assertContains(response, 0)
