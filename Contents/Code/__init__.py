# Kink.com
import re

# URLS
EXC_BASEURL = 'http://www.kink.com/'
EXC_SEARCH_MOVIES = EXC_BASEURL + 'search?q=%s'
EXC_MOVIE_INFO = EXC_BASEURL + 'shoot/%s'
EXC_MODEL_INFO = EXC_BASEURL + 'model/%s'

def Start():
  HTTP.CacheTime = CACHE_1DAY

class KinkAgent(Agent.Movies):
  name = 'Kink.com'
  languages = [Locale.Language.English]
  accepts_from = ['com.plexapp.agents.localmedia']
  primary_provider = True
  sites = dict([
    ("carmenrivera", "Carmen Rivera"),
    ("digitalsin", "Digital Sin"),
    ("amator", "Amator"),
    ("wrestlingmale", "WrestlingMale"),
    ("harmonyfetish", "Harmony Fetish"),
    ("whippedass", "Whipped Ass"),
    ("twistedvisual", "Twisted Visual"),
    ("filthsyndicate", "Filth Syndicate"),
    ("kinkclassics", "Kink Classics"),
    ("severesexfilms", "Severe Sex Films"),
    ("missionaryboyz", "Missionary Boyz"),
    ("povpickups", "POV Pickups"),
    ("hogtied", "Hogtied"),
    ("menatplay", "Men At Play"),
    ("thevenusgirls", "The Venus Girls"),
    ("evolvedfights", "Evolved Fights"),
    ("submissived", "Submissived"),
    ("bondageliberation", "Bondage Liberation"),
    ("ashleyfiresscifidreamgirls", "Ashley Fires SciFi Dreamgirls"),
    ("familydick", "Family Dick"),
    ("everythingbutt", "Everything Butt"),
    ("meanbitch", "Mean Bitch"),
    ("sweetfemdom", "Sweet FemDom"),
    ("boynapped", "Boynapped"),
    ("filthyfemdom", "Filthy Femdom"),
    ("kinkmenclassics", "KinkMen Classics"),
    ("sisterwives", "Sister Wives"),
    ("masqulin", "Masqulin"),
    ("hotlegsandfeet", "Hot Legs &amp; Feet"),
    ("bananajacks", "Banana Jacks"),
    ("devicebondage", "Device Bondage"),
    ("wasteland", "Wasteland"),
    ("alternadudes", "Alternadudes"),
    ("manupfilms", "Man Up Films"),
    ("brutalsessions", "Brutal Sessions"),
    ("kinkfeatures", "Kink Features"),
    ("evolvedfightslesbianedition", "Evolved Fights Lesbian Edition"),
    ("machinedom", "Machine Dom"),
    ("pascalssubsluts", "Pascals Sub Sluts"),
    ("medicalysado", "Medical y Sado"),
    ("hardcorepunishments", "Hardcore Punishments"),
    ("fembotacademy", "Fembot Academy"),
    ("tsseduction", "TS Seduction"),
    ("titanmenrough", "TitanMen Rough"),
    ("hogtiedup", "Hogtied Up"),
    ("kinkybites", "Kinky Bites"),
    ("sexandsubmission", "Sex And Submission"),
    ("tspussyhunters", "TS Pussy Hunters"),
    ("kinkybitesmen", "Kinky Bites Men"),
    ("fuckingmachines", "Fucking Machines"),
    ("pegging", "Pegging"),
    ("bifuck", "BiFUCK"),
    ("mondofetiche", "Mondo Fetiche"),
    ("ballgaggers", "Ball Gaggers"),
    ("pornstarplatinum", "Pornstar Platinum"),
    ("strugglingbabes", "Struggling Babes"),
    ("houseoftaboo", "House of Taboo"),
    ("submissivex", "Submissive X"),
    ("ddfnetwork", "DDF Network"),
    ("tormenttime", "Torment Time"),
    ("peghim", "PegHim"),
    ("bizarrevideo", "Bizarre Video"),
    ("spizoo", "Spizoo"),
    ("femmefatalefilms", "Femme Fatale Films"),
    ("boundandgagged", "Bound And Gagged"),
    ("lakeviewentertainment", "Lakeview Entertainment"),
    ("swnude", "SW Nude"),
    ("str8hell", "Str8Hell"),
    ("royalfetishfilms", "Royal Fetish Films"),
    ("transerotica", "TransErotica"),
    ("cfnmeu", "CFNMEU"),
    ("gloryholesecrets", "Gloryhole Secrets"),
    ("azianiiron", "Aziani Iron"),
    ("mydirtiestfantasy", "My Dirtiest Fantasy"),
    ("myfriendsfeet", "My Friends' Feet"),
    ("boundgods", "Bound Gods"),
    ("hardcoregangbang", "Hardcore Gangbang"),
    ("electrosluts", "Electrosluts"),
    ("fetishnetworkmale", "FetishNetwork Male"),
    ("familiestied", "Families Tied"),
    ("boundgangbangs", "Bound Gang Bangs"),
    ("menonedge", "Men On Edge"),
    ("theupperfloor", "The Upper Floor"),
    ("divinebitches", "Divine Bitches"),
    ("boundmenwanked", "Bound Men Wanked"),
    ("bizarrets", "Bizarre Video Transsexual"),
    ("fetishnetwork", "FetishNetwork"),
    ("sexualdisgrace", "Sexual Disgrace"),
    ("reluctantyoungmen", "Reluctant Young Men"),
    ("bleufilms", "Bleu Films"),
    ("bonusholeboys", "Bonus Hole Boys"),
    ("publicdisgrace", "Public Disgrace"),
    ("straponsquad", "Strapon Squad"),
    ("waterbondage", "Water Bondage"),
    ("gentlemenscloset", "Gentlemens Closet"),
    ("ultimatesurrender", "Ultimate Surrender"),
    ("plumperd", "Plumperd"),
    ("revengeofthebaroness", "Revenge Of The Baroness"),
    ("nastydaddy", "Nasty Daddy"),
    ("yesirboys", "Yesirboys"),
    ("femdum", "FemDum"),
    ("captivemale", "Captive Male"),
    ("thetrainingofo", "The Training Of O"),
    ("chantasbitches", "Chanta's Bitches"),
    ("fuckedandbound", "Fucked and Bound"),
    ("devianthardcore", "Deviant Hardcore"),
    ("30minutesoftorment", "30 Minutes of Torment"),
    ("buttmachineboys", "Butt Machine Boys"),
    ("nakedkombat", "Naked Kombat"),
    ("kinkuniversity", "Kink University"),
    ("boundinpublic", "Bound in Public"),
    ("wiredpussy", "Wired Pussy"),
    ("footworship", "Foot Worship"),
    ("sadisticrope", "Sadistic Rope"),
    ("animatedkink", "Animated Kink"),
    ("meninpain", "Men In Pain"),
    ("kinklive", "KinkLive")
  ])


  # search() gets called with a media arguments like {
  #   'openSubtitlesHash': '0075d46081a49c9c',
  #   'name': 'Sas 3688',
  #   'filename': '%2FVolumes%2FData%2Fkinktest%2FSex%2EAnd%2ESubmission%2FSAS_3688%2F3689%2Emp4',
  #   'plexHash': '4de61af5c49738c2cedfbf3f9c637c07d84e84db',
  #   'duration': '2509148',
  #   'id': '254209'
  # }
  def search(self, results, media, lang):
    Log.Debug('KinkAgent.search() was called')

    title = media.name
    if media.primary_metadata is not None:
      Log.Debug('title was overridden by primary_metadata.title')
      title = media.primary_metadata.title
    Log.Debug('Got title "' + title + '"')

    # Only direct episode matching by directory names is supported. Directories
    # must match the episode id, i.e.
    #    386, 3823, 102405
    # They may be prepended by a channel abbreviation, i.e.
    #    SAS_38522, FM-23412, DB 2341
    # Supported dividing chars are space, dash and underscore or nothing at all:
    #
    # The channel abbreviation is ignored as the right channel is found by the
    # episode id anyway. Nevertheless it might be your attribute of choice to
    # organize your file system.
    episodeMatch = re.match(r'(?:[A-Za-z]*[ ]?)*(\d{3,})', title)

    if episodeMatch is not None:
      episodeId = episodeMatch.group(1)
      Log.Debug('Matched episdode id ' + episodeId)
      results.Append(MetadataSearchResult(id = episodeId, name = title, score = 90, lang = lang))
    else:
      Log.Debug('Could not match an episode id')

    results.Sort('score', descending=True)

  def update(self, metadata, media, lang):
    Log.Debug('KinkAgent.update() has been called')
    html = HTML.ElementFromURL(EXC_MOVIE_INFO % metadata.id,
                               headers={'Cookie': 'viewing-preferences=straight%2Cgay'})

    # use site name as movie studio
    # add site name to genres
    metadata.genres.clear()
    try:
      sitename = html.xpath('//div[@class="shoot-page"]/@data-sitename')[0]
      metadata.studio = KinkAgent.sites[sitename.strip()]
    except: pass

    # add channels to genres
    # add other tags to collections
    metadata.collections.clear()
    unaccepted_tags = ['bareback', 'airtight playlist', 'anal fingering', 'anal fisting', 'anal stretching', 'best of sas', 'anal creampie', 'blindfold', 'blowjob', 'sadism', 'smothering', 'takedown', 'the chair', 'high heels', 'mixed', 'mind fuck', 'muscle', 'leather belt', 'leather cuffs', 'lingerie', 'bush', 'sub', 'cop', 'feet', 'fingerine', 'fisting', 'gaping', 'role play', 'fetish', 'curvy', 'foreskin', 'uniform', 'hair pulling', 'kinky', 'noose', 'vaginal fisting', 'versatile', 'zapper', 'rimming', 'top', 'stud', 'muscular', 'toned', 'belly punching', 'smoking', 'teacher', 'tied outside', 'outdoors', 'pierced nipples', 'pierced pussy', 'medical fetish', 'discipline', 'hairy', 'kidnapping play', 'straight', 'tattoo', 'big ass', 'bit gag', 'black', 'body builder', 'boot worship', 'bottom', 'brunet', 'blond', 'brutal cockolding', 'brutal punishment', 'cbt', 'champion', 'chastity play', 'christmas', 'circumcised', 'uncircumcised', 'clothespins', 'shaped', 'hand gagging', 'slave', 'female slave', 'nurse', 'submission', 'eighteen and...', 'unshaved', 'other hair color', 'romance', 'oral sex', 'milf', 'domination', 'bdsm', 'chains', 'mask', 'cage', 'choking', 'crop', 'latinx', 'lift and carry', 'rough sex', 'destruction', 'cock and ball torture', 'collar', 'domestic', 'dunking', 'doctor', 'dildo', 'dungeon', 'ebony', 'electro plug']

    #tags = html.xpath('//a[starts-with(@href,"/tag/")]')
    tags = html.xpath('//p[@class="tag-list category-tag-list"]/a[starts-with(@href,"/tag/")]')
    for tag in tags:
      if not tag.text_content().strip().lower() in unaccepted_tags :
        metadata.genres.add(tag.text_content().strip().title())

    #if tag.get('href').endswith(':channel'):
    #if not metadata.studio:
    #metadata.studio = tag.text_content().strip()
    #metadata.genres.add(tag.text_content().strip())
    #else:
    #metadata.collections.add(tag.text_content().strip())

    # set movie title to shoot title
    metadata.title = html.xpath('//div[@class="shoot-content"]//h1[@class="shoot-title"]/text()')[0] + " (" + metadata.id + ")"

    # set content rating to XXX
    metadata.content_rating = 'XXX'

    # set episode ID as tagline for easy visibility
    metadata.tagline = metadata.studio + " – " + metadata.id

    # set movie release date to shoot release date
    try:
      release_date = html.xpath('//*[@class="shoot-date"]/text()')[0]
      metadata.originally_available_at = Datetime.ParseDate(release_date).date()
      metadata.year = metadata.originally_available_at.year
    except: pass

    # set poster to the image that kink.com chose as preview
    try:
      thumbpUrl = html.xpath('//video/@poster')[0]
      thumbp = HTTP.Request(thumbpUrl)
      metadata.posters[thumbpUrl] = Proxy.Media(thumbp)
    except: pass

    # fill movie art with all images, so they can be used as backdrops
    try:
      #imgs = html.xpath('//div[@id="previewImages"]//img')
      imgs = html.xpath('//div[@id="gallerySlider"]//img')
      for img in imgs:
        thumbUrl = re.sub(r'/h/[0-9]{3,3}/', r'/h/830/', img.get('src'))
        thumb = HTTP.Request(thumbUrl)
        metadata.art[thumbUrl] = Proxy.Media(thumb)
    except: pass

    # summary
    try:
      metadata.summary = ""
      #summary1 = html.xpath('//p[@class="tag-list category-tag-list"]/a[starts-with(@href,"/tag/")]')
      summary1 = html.xpath('//*[@name="description"]/@content')[0]
      metadata.summary = summary1
    except: pass

    # director
    try:
      metadata.directors.clear()
      director_name = html.xpath('//*[@class="director-name"]/a/text()')[0]
      try:
        director = metadata.directors.new()
        director.name = director_name
      except:
        try:
          metadata.directors.add(director_name)
        except: pass
    except: pass

    # starring
    try:
      starring = html.xpath('//p[@class="starring"]//a//text()')
      metadata.roles.clear()
      for member in starring:
        role = metadata.roles.new()
        try:
          role.name = member.replace(',', '')
        except:
          try:
            role.actor = member.replace(',', '')
          except: pass
    except: pass

    # rating
    try:
      rating_dict = JSON.ObjectFromURL(url=EXC_BASEURL + 'api/ratings/%s' % metadata.id,
                                       headers={'Cookie': 'viewing-preferences=straight%2Cgay'})
      metadata.rating = float(rating_dict['average']) * 2
    except: pass
