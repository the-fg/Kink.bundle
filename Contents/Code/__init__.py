# Kink.com
import re

# URLS
EXC_BASEURL = 'http://www.kink.com'
EXC_SEARCH_MOVIES = EXC_BASEURL + '/search?q=%s'
EXC_MOVIE_INFO = EXC_BASEURL + '/shoot/%s'

def Start():
    HTTP.CacheTime = CACHE_1DAY

class KinkAgent(Agent.Movies):
    name = 'Kink.com'
    languages = [Locale.Language.English]
    accepts_from = ['com.plexapp.agents.localmedia']
    primary_provider = True
    channels = dict([
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

        # Use channel name as the movie studio to be able to select movies by channel
        try:
            sitename = html.xpath('//div[@class="shoot-page"]/@data-sitename')[0]
            studio = KinkAgent.channels[sitename.strip()]
            Log.Debug('Got channel "' + sitename.strip() + '", set studio to "' + studio + '"')
            metadata.studio = studio
        except: pass

        # Previously the collection field was prefilled with the tags but that's not
        # that useful. Users might want to regain collecitons for the other purposes.
        # Clear them here if not locked by manual edits.
        metadata.collections.clear()

        # Add shoot tags to tag genre
        # TODO : expose preferences for users to add unacceptable tags
        #unaccepted_tags = ['bareback', 'airtight playlist', 'anal fingering', 'anal fisting', 'anal stretching', 'best of sas', 'anal creampie', 'blindfold', 'blowjob', 'sadism', 'smothering', 'takedown', 'the chair', 'high heels', 'mixed', 'mind fuck', 'muscle', 'leather belt', 'leather cuffs', 'lingerie', 'bush', 'sub', 'cop', 'feet', 'fingerine', 'fisting', 'gaping', 'role play', 'fetish', 'curvy', 'foreskin', 'uniform', 'hair pulling', 'kinky', 'noose', 'vaginal fisting', 'versatile', 'zapper', 'rimming', 'top', 'stud', 'muscular', 'toned', 'belly punching', 'smoking', 'teacher', 'tied outside', 'outdoors', 'pierced nipples', 'pierced pussy', 'medical fetish', 'discipline', 'hairy', 'kidnapping play', 'straight', 'tattoo', 'big ass', 'bit gag', 'black', 'body builder', 'boot worship', 'bottom', 'brunet', 'blond', 'brutal cockolding', 'brutal punishment', 'cbt', 'champion', 'chastity play', 'christmas', 'circumcised', 'uncircumcised', 'clothespins', 'shaped', 'hand gagging', 'slave', 'female slave', 'nurse', 'submission', 'eighteen and...', 'unshaved', 'other hair color', 'romance', 'oral sex', 'milf', 'domination', 'bdsm', 'chains', 'mask', 'cage', 'choking', 'crop', 'latinx', 'lift and carry', 'rough sex', 'destruction', 'cock and ball torture', 'collar', 'domestic', 'dunking', 'doctor', 'dildo', 'dungeon', 'ebony', 'electro plug']
        ignore_tags = []
        # Clear out any existing tags and add all available
        metadata.genres.clear()
        tagNodes = html.xpath('//p[@class="tag-list category-tag-list"]/a[starts-with(@href,"/tag/")]')
        for node in tagNodes:
            tag = node.text_content().strip().lower()
            if not tag in ignore_tags:
                metadata.genres.add(tag)
                Log.Debug('Added tag "%s"' % tag)
            else:
                Log.Debug('Ignored tag "%s"' % tag)

        # set movie title to shoot title
        metadata.title = html.xpath('//div[@class="shoot-content"]//h1[@class="shoot-title"]/text()')[0] + " (" + metadata.id + ")"
        Log.Debug('Set shoot title to "%s"' % metadata.title)

        # set content rating to XXX
        metadata.content_rating = 'XXX'

        # Set episode ID as tagline for easy visibility
        # Still do this though the tagline is not shown anymore
        metadata.tagline = metadata.studio + " – " + metadata.id
        Log.Debug('Set tagline to "%s"' % metadata.tagline)

        # set movie release date to shoot release date
        try:
            release_date = html.xpath('//*[@class="shoot-date"]/text()')[0]
            metadata.originally_available_at = Datetime.ParseDate(release_date).date()
            metadata.year = metadata.originally_available_at.year
            Log.Debug('Set shoot date to "%s"' % metadata.originally_available_at.strftime('%Y-%m-%d'))
            Log.Debug('Set shoot year to "%s"' % metadata.year)
        except Exception,e:
            Log.Error('Error obaining shoot date for shoot %s [%s]', metadata.id, e.message)

        # Set poster to the image that kink.com chose as preview image
        try:
            thumbpUrl = html.xpath('//video/@poster')[0]
            thumbp = HTTP.Request(thumbpUrl)
            metadata.posters[thumbpUrl] = Proxy.Media(thumbp)
            Log.Debug('Added video preview image found at "%s"', thumbpUrl)
        except Exception,e:
            Log.Error('Error obaining shoot images for shoot %s [%s]', metadata.id, e.message)

        # Fill all images found for the shoot to both posters and art to be able to
        # to choose whichever suits best depending on the theme.
        try:
            imgs = html.xpath('//div[@id="gallerySlider"]//img')
            numImgs = 0
            for img in imgs:
                #thumbUrl = re.sub(r'/h/[0-9]{3,3}/', r'/h/830/', img.get('src'))
                thumbUrl = img.get('data-image-file')
                thumb = HTTP.Request(thumbUrl)
                metadata.posters[thumbUrl] = Proxy.Media(thumb)
                metadata.art[thumbUrl] = Proxy.Media(thumb)
                Log.Debug('Adding immage "%s"', thumbUrl)
                numImgs+=1
            Log.Debug('Added a total of %s images' % numImgs)
        except Exception,e:
            Log.Error('Error obaining shoot images for shoot %s [%s]', metadata.id, e.message)

        # Plot summary
        metadata.summary = ""
        try:
            metadata.summary = html.xpath('//meta[@name="description"]/@content')[0]
            Log.Debug('Set shoot summary to "%s"' % metadata.summary)
        except Exception,e:
            Log.Error('Error obaining summary for shoot %s [%s]', metadata.id, e.message)

        # Director
        metadata.directors.clear()
        try:
            director_name = html.xpath('//*[@class="director-name"]/a/text()')[0]
            director = metadata.directors.new()
            director.name = director_name
            Log.Debug('Added shoot director "%s"' % director.name)
        except Exception,e:
            Log.Error('Error obaining director for shoot %s [%s]', metadata.id, e.message)

        # Add models
        metadata.roles.clear()
        try:
            models = html.xpath('//p[@class="starring"]//a')
            Log.Debug('Proccessing %s models found' % len(models))
            for model in models:
                Log.Debug('Fetching model with URL "%s"' % model.get('href'))
                modelHtml = HTML.ElementFromURL(EXC_BASEURL + model.get('href'),
                                                headers={'Cookie': 'viewing-preferences=straight%2Cgay'})

                bioData = modelHtml.xpath('//div[contains(@class, "bio-favorite")]')[0]
                # Fetch first bio slider image to use as photo
                imgData = modelHtml.xpath('//img[contains(@class, "bio-slider-img")]')[0]

                role = metadata.roles.new()
                role.name = bioData.get('data-title')
                role.photo = imgData.get('src')
                Log.Debug('Stored model "%s" with photo "%s"', role.name, role.photo)
        except Exception,e:
            Log.Error('Error obtaining performers for shoot %s [%s]', metadata.id, e.message)

        # Shoot Rating
        try:
            ratingData = JSON.ObjectFromURL(url=EXC_BASEURL + '/api/ratings/%s' % metadata.id,
                                            headers={'Cookie': 'viewing-preferences=straight%2Cgay'})
            metadata.rating = float(ratingData['ratingPositiveCount'])/float(ratingData['ratingCount']) * 10
            Log.Debug('Set shoot rating to "%s"' % metadata.rating)
        except Exception,e:
            Log.Error('Error obaining rating for shoot %s [%s]', metadata.id, e.message)
