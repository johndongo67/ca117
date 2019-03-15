import re

phone = r'\b\d{2,3}[-\s]{1}\d{7}\b'

email = r'\b(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*\b'

ldate = r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2,4}'

date = r'\b\d{1,2}\W\d{1,2}\W\d{2}\b'
