from flask import Blueprint, render_template

bp = Blueprint('views', __name__)

@bp.route('/')
@bp.route('/index.html')
def index():
    """Home page."""
    hero_content = {
        'title': 'Florence Nightingale',
        'subtitle': 'The Lady with the Lamp',
        'description': 'Pioneer of modern nursing, statistician, and social reformer (1820-1910)',
        'image_url': 'https://image.coze.run/?prompt=Portrait%20of%20Florence%20Nightingale%20in%20Victorian%20era%20style%2C%20wearing%20a%20dark%20dress%20with%20white%20collar%2C%20holding%20a%20lamp&image_size=portrait_4_3'
    }

    quick_facts = [
        {'year': '1820', 'fact': 'Born in Florence, Italy'},
        {'year': '1854', 'fact': 'Led nurses in the Crimean War'},
        {'year': '1860', 'fact': 'Founded the first secular nursing school'},
        {'year': '1910', 'fact': 'Left a lasting legacy in modern healthcare'}
    ]

    return render_template('index.html',
                         hero_content=hero_content,
                         quick_facts=quick_facts)

@bp.route('/timeline.html')
def timeline():
    """Timeline page."""
    timeline_events = [
        {
            'date': 'May 12, 1820',
            'title': 'Birth in Florence',
            'description': 'Born in Florence, Italy, to wealthy British parents William and Frances Nightingale.',
            'image_url': 'https://image.coze.run/?prompt=Historical%20painting%20of%20Florence%2C%20Italy%20in%201820&image_size=landscape_4_3'
        },
        {
            'date': '1844',
            'title': 'Divine Calling',
            'description': 'Received what she believed to be a divine calling from God to serve as a nurse, facing strong opposition from her family.',
            'image_url': 'https://image.coze.run/?prompt=Victorian%20era%20young%20woman%20in%20contemplation%20by%20window&image_size=portrait_4_3'
        },
        {
            'date': '1851',
            'title': 'Nursing Training',
            'description': 'Studied nursing at the Institute of Protestant Deaconesses in Kaiserswerth, Germany.',
            'image_url': 'https://image.coze.run/?prompt=Historical%20hospital%20ward%20in%20Germany%201850s&image_size=landscape_4_3'
        },
        {
            'date': '1853',
            'title': 'First Superintendent Role',
            'description': 'Became superintendent at the Institute for the Care of Sick Gentlewomen in London.',
            'image_url': 'https://image.coze.run/?prompt=Victorian%20London%20hospital%20exterior%201850s&image_size=landscape_4_3'
        },
        {
            'date': 'October 21, 1854',
            'title': 'Crimean War Service',
            'description': 'Led a team of 38 nurses to the Crimean War, serving at the Barrack Hospital in Scutari.',
            'image_url': 'https://image.coze.run/?prompt=Florence%20Nightingale%20with%20lamp%20in%20hospital%20ward%20Crimean%20War&image_size=landscape_4_3'
        },
        {
            'date': '1855',
            'title': 'Hospital Reforms',
            'description': 'Implemented revolutionary sanitation practices at Scutari, dramatically reducing mortality rates.',
            'image_url': 'https://image.coze.run/?prompt=Victorian%20era%20hospital%20ward%20being%20cleaned&image_size=landscape_4_3'
        },
        {
            'date': '1859',
            'title': 'Notes on Nursing',
            'description': 'Published "Notes on Nursing," which became the cornerstone of modern nursing education.',
            'image_url': 'https://image.coze.run/?prompt=Old%20book%20cover%20Notes%20on%20Nursing%201859&image_size=portrait_4_3'
        },
        {
            'date': '1860',
            'title': 'Nightingale School',
            'description': 'Established the Nightingale Training School at St Thomas\' Hospital, London.',
            'image_url': 'https://image.coze.run/?prompt=St%20Thomas%20Hospital%20London%201860&image_size=landscape_4_3'
        },
        {
            'date': '1907',
            'title': 'Order of Merit',
            'description': 'Became the first woman to receive the Order of Merit from King Edward VII.',
            'image_url': 'https://image.coze.run/?prompt=Order%20of%20Merit%20medal%20Victorian%20era&image_size=square'
        },
        {
            'date': 'August 13, 1910',
            'title': 'Death and Legacy',
            'description': 'Passed away in London, leaving an enduring legacy in modern healthcare and nursing education.',
            'image_url': 'https://image.coze.run/?prompt=Victorian%20memorial%20statue%20of%20Florence%20Nightingale&image_size=portrait_4_3'
        }
    ]
    return render_template('timeline.html', timeline_events=timeline_events)

@bp.route('/gallery.html')
def gallery():
    """Gallery page."""
    gallery_items = [
        {
            'title': 'Portrait of Florence Nightingale',
            'description': 'A formal portrait of Florence Nightingale in her younger years, circa 1850.',
            'image_url': 'https://image.coze.run/?prompt=Portrait%20of%20young%20Florence%20Nightingale%20in%20Victorian%20style&image_size=portrait_4_3',
            'category': 'portraits'
        },
        {
            'title': 'The Lady with the Lamp',
            'description': 'Florence Nightingale making her rounds in the military hospital at Scutari.',
            'image_url': 'https://image.coze.run/?prompt=Florence%20Nightingale%20with%20lamp%20in%20dark%20hospital%20ward&image_size=landscape_4_3',
            'category': 'crimean_war'
        },
        {
            'title': 'Scutari Hospital',
            'description': 'The exterior of Barrack Hospital at Scutari where Nightingale worked during the Crimean War.',
            'image_url': 'https://image.coze.run/?prompt=Historical%20Barrack%20Hospital%20at%20Scutari%201855&image_size=landscape_4_3',
            'category': 'locations'
        },
        {
            'title': 'Notes on Nursing',
            'description': 'First edition cover of her seminal work "Notes on Nursing" published in 1859.',
            'image_url': 'https://image.coze.run/?prompt=Vintage%20book%20cover%20Notes%20on%20Nursing%201859&image_size=portrait_4_3',
            'category': 'publications'
        },
        {
            'title': 'Statistical Diagrams',
            'description': 'The famous "Rose Diagram" showing causes of mortality in the army.',
            'image_url': 'https://image.coze.run/?prompt=Florence%20Nightingale%20Rose%20Diagram%20statistical%20chart&image_size=square',
            'category': 'work'
        },
        {
            'title': 'Nightingale Training School',
            'description': 'St Thomas\' Hospital where the first Nightingale Training School was established.',
            'image_url': 'https://image.coze.run/?prompt=St%20Thomas%20Hospital%20London%201860%20exterior&image_size=landscape_4_3',
            'category': 'locations'
        },
        {
            'title': 'Family Home',
            'description': 'Lea Hurst, the Nightingale family home in Derbyshire.',
            'image_url': 'https://image.coze.run/?prompt=Victorian%20mansion%20Lea%20Hurst%20Derbyshire&image_size=landscape_4_3',
            'category': 'locations'
        },
        {
            'title': 'Military Hospital Ward',
            'description': 'A ward in the military hospital at Scutari after Nightingale\'s improvements.',
            'image_url': 'https://image.coze.run/?prompt=Clean%20organized%20Victorian%20military%20hospital%20ward&image_size=landscape_4_3',
            'category': 'crimean_war'
        },
        {
            'title': 'Nursing Students',
            'description': 'Early students at the Nightingale Training School in their uniforms.',
            'image_url': 'https://image.coze.run/?prompt=Victorian%20era%20nursing%20students%20in%20uniforms&image_size=landscape_4_3',
            'category': 'education'
        },
        {
            'title': 'Letter Manuscript',
            'description': 'A handwritten letter by Florence Nightingale discussing hospital conditions.',
            'image_url': 'https://image.coze.run/?prompt=Victorian%20era%20handwritten%20letter%20manuscript&image_size=portrait_4_3',
            'category': 'documents'
        },
        {
            'title': 'Order of Merit',
            'description': 'The Order of Merit awarded to Nightingale by King Edward VII in 1907.',
            'image_url': 'https://image.coze.run/?prompt=British%20Order%20of%20Merit%20medal%20Victorian%20era&image_size=square',
            'category': 'awards'
        },
        {
            'title': 'Memorial Statue',
            'description': 'The Florence Nightingale memorial statue in London.',
            'image_url': 'https://image.coze.run/?prompt=Bronze%20memorial%20statue%20of%20Florence%20Nightingale&image_size=portrait_4_3',
            'category': 'memorials'
        },
        {
            'title': 'Birth Place',
            'description': 'Villa Colombaia in Florence, Italy, where Nightingale was born.',
            'image_url': 'https://image.coze.run/?prompt=Italian%20villa%20in%20Florence%201820s%20architecture&image_size=landscape_4_3',
            'category': 'locations'
        },
        {
            'title': 'Statistical Work',
            'description': 'Nightingale at work on her statistical analyses and reports.',
            'image_url': 'https://image.coze.run/?prompt=Victorian%20woman%20working%20at%20desk%20with%20papers%20and%20charts&image_size=landscape_4_3',
            'category': 'work'
        },
        {
            'title': 'Final Portrait',
            'description': 'One of the last photographs taken of Florence Nightingale, circa 1907.',
            'image_url': 'https://image.coze.run/?prompt=Elderly%20Florence%20Nightingale%20formal%20portrait%20Victorian%20era&image_size=portrait_4_3',
            'category': 'portraits'
        }
    ]
    return render_template('gallery.html', gallery_items=gallery_items)

@bp.route('/quotes.html')
def quotes():
    """Quotes page."""
    quotes_data = [
        {
            'quote': 'I attribute my success to this - I never gave or took any excuse.',
            'source': 'Letter to a friend, 1861',
            'category': 'Personal Philosophy',
            'context': 'Discussing her determination in face of obstacles',
            'year': '1861'
        },
        {
            'quote': 'The very first requirement in a hospital is that it should do the sick no harm.',
            'source': 'Notes on Hospitals, 1859',
            'category': 'Healthcare',
            'context': 'On the importance of hospital sanitation',
            'year': '1859'
        },
        {
            'quote': 'Nursing is an art: and if it is to be made an art, it requires an exclusive devotion as hard a preparation as any painter\'s or sculptor\'s work.',
            'source': 'Notes on Nursing',
            'category': 'Nursing',
            'context': 'Describing the professional nature of nursing',
            'year': '1859'
        },
        {
            'quote': 'I think one\'s feelings waste themselves in words; they ought all to be distilled into actions which bring results.',
            'source': 'Letter to Benjamin Jowett',
            'category': 'Action',
            'context': 'On the importance of practical action',
            'year': '1861'
        },
        {
            'quote': 'The greatest heroes are those who do their duty in the daily grind of domestic affairs whilst the world whirls as a maddening dreidel.',
            'source': 'Private Notes',
            'category': 'Duty',
            'context': 'Reflecting on everyday heroism',
            'year': '1870'
        },
        {
            'quote': 'How very little can be done under the spirit of fear.',
            'source': 'Letter to a Nurse',
            'category': 'Courage',
            'context': 'Encouraging bravery in nursing practice',
            'year': '1867'
        },
        {
            'quote': 'Rather, ten times, die in the surf, heralding the way to a new world, than stand idly on the shore.',
            'source': 'Personal Journal',
            'category': 'Leadership',
            'context': 'On taking initiative and leading change',
            'year': '1850'
        },
        {
            'quote': 'For the sick it is important to have the best.',
            'source': 'Notes on Nursing',
            'category': 'Healthcare',
            'context': 'On quality of care',
            'year': '1859'
        },

        {
            'quote': 'The world is put back by the death of every one who has to sacrifice the development of his or her peculiar gifts to conventionality.',
            'source': 'Cassandra',
            'category': 'Personal Growth',
            'context': 'On societal constraints',
            'year': '1852'
        },
        {
            'quote': 'I am of certain convinced that the greatest heroes are those who do their duty in the daily grind of domestic affairs whilst the world whirls as a maddening dreidel.',
            'source': 'Private Notes',
            'category': 'Duty',
            'context': 'On everyday heroism',
            'year': '1870'
        },
        {
            'quote': 'Were there none who were discontented with what they have, the world would never reach anything better.',
            'source': 'Suggestions for Thought',
            'category': 'Progress',
            'context': 'On the importance of seeking improvement',
            'year': '1860'
        },
        {
            'quote': 'Live life when you have it. Life is a splendid gift-there is nothing small about it.',
            'source': 'Letter to Student Nurses',
            'category': 'Life Philosophy',
            'context': 'Advice to young nurses',
            'year': '1872'
        },
        {
            'quote': 'To understand God\'s thoughts we must study statistics, for these are the measure of his purpose.',
            'source': 'Notes on Nursing',
            'category': 'Statistics',
            'context': 'On the importance of data in healthcare',
            'year': '1859'
        },
        {
            'quote': 'The most important practical lesson that can be given to nurses is to teach them what to observe.',
            'source': 'Notes on Nursing',
            'category': 'Nursing Education',
            'context': 'On nursing observation skills',
            'year': '1859'
        },
        {
            'quote': 'Never give nor take an excuse.',
            'source': 'Letter to Nurses',
            'category': 'Personal Philosophy',
            'context': 'On personal responsibility',
            'year': '1861'
        },
        {
            'quote': 'The element of time is the chief difference between success and failure.',
            'source': 'Hospital Notes',
            'category': 'Success',
            'context': 'On timing in healthcare',
            'year': '1863'
        },
        {
            'quote': 'I stand at the altar of the murdered men, and, while I live, I fight their cause.',
            'source': 'Letter during Crimean War',
            'category': 'Advocacy',
            'context': 'On advocating for soldiers',
            'year': '1856'
        },
        {
            'quote': 'Wise and humane management of the patient is the best safeguard against infection.',
            'source': 'Notes on Nursing',
            'category': 'Patient Care',
            'context': 'On preventing disease spread',
            'year': '1859'
        },
        {
            'quote': 'Everything is sketchy. The world does nothing but sketch.',
            'source': 'Personal Journal',
            'category': 'Philosophy',
            'context': 'Reflecting on life\'s impermanence',
            'year': '1855'
        },
        {
            'quote': 'Let whoever is in charge keep this simple question in her head (not, how can I always do this right thing myself, but) how can I provide for this right thing to be always done?',
            'source': 'Notes on Nursing',
            'category': 'Leadership',
            'context': 'On systematic improvement',
            'year': '1859'
        }
    ]
    return render_template('quotes.html', quotes=quotes_data)

@bp.route('/impact.html')
def impact():
    """Impact page."""
    impact_data = {
        'hero': {
            'title': 'The Lasting Impact of Florence Nightingale',
            'subtitle': 'How the Lady with the Lamp Illuminated Modern Healthcare',
            'image_url': 'https://image.coze.run/?prompt=Florence%20Nightingale%20legacy%20modern%20nursing%20symbolic%20artwork&image_size=landscape_16_9'
        },
        'sections': [
            {
                'id': 'nursing-education',
                'title': 'Nursing Education',
                'content': '''Florence Nightingale revolutionized nursing education by establishing the first secular nursing school at St Thomas' Hospital in London in 1860. This pioneering institution set the standard for professional nursing education worldwide. Her approach emphasized both theoretical knowledge and practical training, introducing a systematic curriculum that included anatomy, hygiene, and patient care techniques.

The Nightingale Training School's success led to the rapid establishment of similar institutions across Britain, Europe, and North America. Her educational principles—combining scientific knowledge with compassionate care—remain fundamental to nursing education today. The school's graduates, known as "Nightingale Nurses," spread her methods globally, establishing nursing schools and improving hospital care worldwide.

Nightingale's emphasis on observation and documentation in nursing education created the foundation for evidence-based nursing practice. Her insistence on maintaining detailed patient records and analyzing healthcare outcomes continues to influence modern nursing education and practice.''',
                'image_url': 'https://image.coze.run/?prompt=Victorian%20era%20nursing%20school%20classroom%20with%20students%20and%20instructor&image_size=landscape_4_3'
            },
            {
                'id': 'hospital-management',
                'title': 'Hospital Management',
                'content': '''Nightingale's contributions to hospital management were revolutionary and continue to influence healthcare facilities today. During the Crimean War, she demonstrated how proper sanitation, ventilation, and organization could dramatically reduce mortality rates. Her reforms at the Scutari Hospital reduced the death rate from 42% to 2% within six months.

She introduced numerous innovations in hospital design and management:
- Ward design principles emphasizing natural light and ventilation
- Systematic cleaning protocols
- Efficient layout of nursing stations
- Separation of clean and dirty utility areas
- Implementation of patient monitoring systems

Her book "Notes on Hospitals" (1859) became the definitive guide for hospital construction and management throughout the Victorian era. Many of her principles, such as the importance of hospital hygiene and the efficient use of space, remain relevant in modern hospital design.

Nightingale's emphasis on collecting and analyzing hospital statistics laid the groundwork for modern healthcare quality improvement programs. Her methods for tracking patient outcomes and hospital performance are predecessors to contemporary healthcare metrics and quality assurance systems.''',
                'image_url': 'https://image.coze.run/?prompt=Modern%20hospital%20ward%20design%20showing%20Florence%20Nightingale%20influence&image_size=landscape_4_3'
            },
            {
                'id': 'public-health',
                'title': 'Public Health',
                'content': '''Nightingale's influence on public health reform was profound and far-reaching. Her statistical evidence and advocacy led to major improvements in military and civilian healthcare systems. She was instrumental in promoting the importance of sanitation, clean water, and proper sewage disposal in public health.

Key contributions to public health include:
- Advocacy for sanitary reform in India
- Promotion of health education for the poor
- Development of community health nursing
- Implementation of systematic health data collection

Her work significantly influenced the passage of the Public Health Act of 1875 in Britain, which established modern public health practices. She demonstrated the connection between living conditions and health outcomes, promoting preventive medicine and population health management.

Nightingale's emphasis on environmental factors in health and disease prevention continues to influence modern public health approaches. Her work laid the foundation for contemporary health promotion and disease prevention strategies.''',
                'image_url': 'https://image.coze.run/?prompt=Public%20health%20campaign%20Victorian%20era%20sanitation%20education&image_size=landscape_4_3'
            },
            {
                'id': 'nursing-ethics',
                'title': 'Nursing Ethics',
                'content': '''Florence Nightingale established fundamental principles of nursing ethics that continue to guide the profession. She elevated nursing from a menial occupation to a respected profession, emphasizing the importance of moral character and professional conduct.

Her ethical principles included:
- Commitment to patient welfare
- Professional confidentiality
- Duty of care
- Personal integrity
- Continuous self-improvement

Nightingale's emphasis on the moral dimensions of nursing helped establish nursing as a calling rather than merely an occupation. Her insistence on high moral standards in nursing practice influenced the development of professional codes of ethics in healthcare.

Her writings on nursing ethics continue to influence modern healthcare ethics, particularly in areas such as:
- Patient advocacy
- Professional responsibility
- Cultural sensitivity
- Evidence-based practice
- Commitment to lifelong learning''',
                'image_url': 'https://image.coze.run/?prompt=Modern%20nurse%20caring%20for%20patient%20professional%20ethical%20care&image_size=landscape_4_3'
            },
            {
                'id': 'statistics',
                'title': 'Statistical Contributions',
                'content': '''Nightingale was a pioneering statistician who revolutionized the use of statistics in healthcare and public policy. She developed innovative methods of presenting statistical data, including the "Nightingale Rose Diagram" (polar area diagram), which demonstrated the causes of mortality in the Crimean War.

Her statistical innovations included:
- Development of graphical presentations of statistics
- Use of comparative statistics in hospital management
- Application of statistical analysis to public health
- Integration of statistics in healthcare planning

Nightingale's statistical work influenced:
- Modern epidemiology
- Healthcare quality metrics
- Evidence-based medicine
- Health services research
- Public health policy

She was the first female member of the Royal Statistical Society and was later elected to the American Statistical Association. Her methods of collecting and analyzing healthcare data laid the foundation for modern healthcare statistics and quality improvement programs.''',
                'image_url': 'https://image.coze.run/?prompt=Florence%20Nightingale%20Rose%20Diagram%20statistical%20chart%20detailed&image_size=square'
            },
            {
                'id': 'international-influence',
                'title': 'International Influence',
                'content': '''Nightingale's influence extended far beyond Britain, shaping healthcare systems worldwide. Her methods and principles were adopted globally, influencing nursing education and healthcare delivery across continents.

International impact areas include:
- Establishment of nursing schools worldwide
- Development of military medical services
- Implementation of hospital reforms globally
- Influence on international health organizations

Her work directly influenced healthcare development in:
- United States (through Linda Richards)
- India (through sanitary reforms)
- Japan (through nursing education)
- Australia (through hospital design)
- Canada (through nursing standards)

Nightingale's principles continue to influence international healthcare through:
- World Health Organization standards
- International nursing education
- Global health initiatives
- Healthcare facility design
- Public health programs''',
                'image_url': 'https://image.coze.run/?prompt=Global%20map%20showing%20Florence%20Nightingale%20influence%20worldwide%20healthcare&image_size=landscape_16_9'
            }
        ],
        'references': [
            {
                'title': 'Notes on Nursing: What It Is, and What It Is Not',
                'author': 'Florence Nightingale',
                'year': '1859'
            },
            {
                'title': 'Notes on Hospitals',
                'author': 'Florence Nightingale',
                'year': '1859'
            },
            {
                'title': 'Florence Nightingale: The Making of an Icon',
                'author': 'Mark Bostridge',
                'year': '2008'
            },
            {
                'title': 'Florence Nightingale: Mystic, Visionary, Healer',
                'author': 'Barbara Montgomery Dossey',
                'year': '2000'
            },
            {
                'title': 'Statistics in Britain, 1865-1930: The Social Construction of Scientific Knowledge',
                'author': 'Donald MacKenzie',
                'year': '1981'
            }
        ]
    }
    return render_template('impact.html', impact_data=impact_data)