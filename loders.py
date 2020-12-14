from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Join


class HeadHuntersLoader(ItemLoader):
    job_title_out = TakeFirst()
    salary_in = Join()
    salary_out = TakeFirst()
    description_in = Join()
    description_out = TakeFirst()
    employer_url_out = TakeFirst()
    company_name_out = TakeFirst()
    company_url_out = TakeFirst()
    company_desc_out = TakeFirst()