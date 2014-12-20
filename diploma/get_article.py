from Tools.extra_methods import ExtraMethods
from parse_article import ParseArticle

class GetArticleInfo(object):
	def __init__(self):
		self.results = None

	def getArticleInfo(self,link):
		if 'segodnya.ua' in link:
			self.resuts = ParseArticleInfo().fromSegodnya(link)
		elif "unn.com.ua" in link:
			self.resuts = ParseArticleInfo().fromUNN(link)
		elif "interfax.com.ua" in link:
			self.resuts = ParseArticleInfo().fromInterfax(link)
		elif "unian.ua" in link:
			self.resuts = ParseArticleInfo().fromUnian(link)
		elif "censor.net.ua" in link:
			self.resuts = ParseArticleInfo().fromCensor(link)
		elif "pravda.com.ua" in link:
			self.resuts = ParseArticleInfo().fromPravda(link)
		elif "statuspress.com.ua" in link:
			self.resuts = ParseArticleInfo().fromStatuspress(link)
		elif "24tv.ua" in link:
			self.resuts = ParseArticleInfo().from24TV(link)
		elif "glavnoe.ua" in link:
			self.resuts = ParseArticleInfo().fromGlavnoe(link)
		elif "telegraf.com.ua" in link:
			self.resuts = ParseArticleInfo().fromTelegraf(link)
		elif "zaxid.net" in link:
			self.resuts = ParseArticleInfo().fromZaxid(link)
		elif "espreso.tv" in link:
			self.resuts = ParseArticleInfo().fromEspreso(link)
		elif "gordonua.com" in link:
			self.resuts = ParseArticleInfo().fromGordon(link)
		elif "tsn.ua" in link:
			self.resuts = ParseArticleInfo().fromTSN(link)
		elif "expres.ua" in link:
			self.resuts = ParseArticleInfo().fromExpres(link)
		elif "tvi.ua" in link:
			self.resuts = ParseArticleInfo().fromTVI(link)
		elif "glavred.info" in link:
			self.resuts = ParseArticleInfo().fromGlavred(link)
		elif "rbc.ua" in link:
			self.resuts = ParseArticleInfo().fromRBC(link)
		elif "focus.ua" in link:
			self.resuts = ParseArticleInfo().fromFocus(link)
		elif "gazeta.ua" in link:
			self.resuts = ParseArticleInfo().fromGazetaUA(link)
		elif "fakty.ictv.ua" in link:
			self.resuts = ParseArticleInfo().fromICTV(link)
		elif "tyzhden.ua" in link:
			self.resuts = ParseArticleInfo().fromTyzhden(link)
		elif "ukrinform.ua" in link:
			self.resuts = ParseArticleInfo().fromUkrinform(link)
		elif "kp.ua" in link:
			self.resuts = ParseArticleInfo().fromKP(link)
		elif "day.kiev.ua" in link:
			self.resuts = ParseArticleInfo().fromDayKiev(link)
		elif "bbc.co.uk" in link:
			self.resuts = ParseArticleInfo().fromBBCUkraine(link)
		elif "joinfo.ua" in link:
			self.resuts = ParseArticleInfo().fromJoinfo(link)
		elif "vchaspik.ua" in link:
			self.resuts = ParseArticleInfo().fromVchaspik(link)
		elif "depo.ua" in link:
			self.resuts = ParseArticleInfo().fromDepoUA(link)
		elif "ipnews.in.ua" in link:
			self.resuts = ParseArticleInfo().fromIPnews(link)
		elif "newsoboz.org" in link:
			self.resuts = ParseArticleInfo().fromNewsOboz(link)
		elif "news.eizvestia.com" in link:
			self.resuts = ParseArticleInfo().fromEizvestia(link)
		elif "pic.com.ua" in link:
			self.resuts = ParseArticleInfo().fromPIC(link)
		elif "news.finance.ua" in link:
			self.resuts = ParseArticleInfo().fromNewsFinance(link)
		elif "capital.ua" in link:
			self.resuts = ParseArticleInfo().fromCapital(link)
		elif "radiosvoboda.org" in link:
			self.resuts = ParseArticleInfo().fromRadiosvoboda(link)
		elif "nr2.com.ua" in link:
			self.resuts = ParseArticleInfo().fromNR2(link)
		elif "uainfo.org" in link:
			self.resuts = ParseArticleInfo().fromUAInfo(link)
		elif "slovoidilo.ua" in link:
			self.resuts = ParseArticleInfo().fromSlovoiDilo(link)
		elif "btbtv.com.ua" in link:
			self.resuts = ParseArticleInfo().fromBtbTv(link)
		elif "7dniv.info" in link:
			self.resuts = ParseArticleInfo().from7Dniv(link)
		elif "politica-ua.com" in link:
			self.resuts = ParseArticleInfo().fromPoliticaUA(link)
		elif "nvua.net" in link:
			self.resuts = ParseArticleInfo().fromNVUA(link)
		elif "forbes.ua" in link:
			self.resuts = ParseArticleInfo().fromForbesUA(link)
		elif "gazetavv.com" in link:
			self.resuts = ParseArticleInfo().fromGazetaVV(link)
		elif "novosti.dn.ua" in link:
			self.resuts = ParseArticleInfo().fromNovostiDN(link)
		elif "dailylviv.com" in link:
			self.resuts = ParseArticleInfo().fromDailyLviv(link)
		elif "112.ua" in link:
			self.resuts = ParseArticleInfo().from112UA(link)

		self.resuts.append(link)
		return self.resuts








