"""
Base de connaissances experte sur Nantes Métropole.
Contient des informations vérifiées et complètes sur :
- Les Transports (Réseau Naolib, gratuité week-end, vélos Bicloo, navibus, aéroport)
- Les Lieux historiques, culturels et touristiques (Château, Machines de l'Île, Passage Pommeraye, etc.)
- Les Hôtels et hébergements (par quartier et budget)
- La Gastronomie et le terroir nantais
- Les conseils pratiques et itinéraires
"""

KNOWLEDGE_CHUNKS = [
    # ==========================
    # TRANSPORTS & MOBILITÉ
    # ==========================
    {
        "id": "transports_gratuite_weekend",
        "category": "transports",
        "title": "Gratuité des transports en commun le week-end (Réseau Naolib)",
        "keywords": ["gratuit", "gratuits", "gratuite", "weekend", "week-end", "samedi", "dimanche", "ticket", "payer", "naolib", "tan"],
        "content": (
            "À Nantes Métropole, TOUS les transports en commun du réseau Naolib (ex-TAN) sont 100% GRATUITS chaque week-end, "
            "du samedi 00h00 au dimanche 23h59. Cette mesure s'applique à tout le monde sans condition (résidents comme touristes de passage). "
            "Sont inclus : les 3 lignes de tramway, les 2 lignes de Busway (lignes 4 et 5), tous les bus et chronobus, ainsi que les Navibus (navettes fluviales sur la Loire et l'Erdre). "
            "Vous n'avez pas besoin de ticket ni de carte de transport, et vous ne devez rien valider en montant à bord le week-end. "
            "Attention : la navette aéroport express spécifique conserve sa propre tarification."
        )
    },
    {
        "id": "transports_tramway",
        "category": "transports",
        "title": "Lignes de Tramway Naolib à Nantes",
        "keywords": ["tram", "tramway", "lignes", "ligne 1", "ligne 2", "ligne 3", "horaires", "commerce", "gare"],
        "content": (
            "Le réseau de tramway de Nantes compte 3 lignes majeures interconnectées :\n"
            "- Ligne 1 (Verte) : Traverse l'agglomération d'Est en Ouest (François Mitterrand / Jamet <-> Beaujoire / Ranzay). "
            "Elle dessert notamment la Gare SNCF (Sortie Nord), le Château des ducs de Bretagne (Duchesse Anne), l'hypercentre (Commerce) et le Parc des Chantiers / Machines de l'Île (Chantiers Navals).\n"
            "- Ligne 2 (Rouge) : Du Nord au Sud (Orvault Grand Val <-> Gare de Pont Rousseau à Rezé). Elle dessert les campus universitaires, la place du Cirque et l'Erdre.\n"
            "- Ligne 3 (Bleue) : Du Nord-Ouest au Sud (Marcel Paul à Saint-Herblain <-> Neustrie à Bouguenais). Pratique pour relier le pôle Commerce à Neustrie (correspondance bus 38 pour l'aéroport).\n"
            "Fréquence : un tram toutes les 3 à 5 minutes en heure de pointe. Fonctionne de 4h30 à 0h30 en semaine, et jusqu'à 2h30 les vendredis et samedis soir."
        )
    },
    {
        "id": "transports_busway_chronobus",
        "category": "transports",
        "title": "Busway et Chronobus Naolib",
        "keywords": ["busway", "bus", "chronobus", "ligne 4", "ligne 5", "gare sud", "hangar a bananes", "vertou"],
        "content": (
            "Le Busway est un système de bus à haut niveau de service en site propre à haute capacité (véhicules électriques articulés de 24 mètres) :\n"
            "- Ligne 4 : Foch Cathédrale <-> Porte de Vertou, idéale pour traverser le Sud-Loire et rejoindre Vertou.\n"
            "- Ligne 5 : Gare de Nantes Sud <-> Hangar à Bananes. Elle dessert tout l'axe central de l'Île de Nantes, "
            "passant par la Cité des Congrès, le quartier de la Création et les Machines de l'Île, jusqu'aux Anneaux de Buren.\n"
            "Les lignes Chronobus (C1, C2, C3, C6, C9, etc.) complètent le réseau avec un passage toutes les 4 à 8 minutes de 5h00 à minuit."
        )
    },
    {
        "id": "transports_navibus",
        "category": "transports",
        "title": "Navibus : Les navettes fluviales sur la Loire et l'Erdre",
        "keywords": ["navibus", "bateau", "bateaux", "loire", "trentemoult", "gare maritime", "erdre", "traversee"],
        "content": (
            "Les Navibus sont des navettes fluviales régulières intégrées au réseau de transport urbain Naolib (accessibles avec un simple titre de transport urbain et GRATUITS le week-end) :\n"
            "- Navibus Loire Ligne N1 : Relie la 'Gare Maritime' (quai de la Fosse, Nantes) au pittoresque village de marins de 'Trentemoult' (Rezé) en seulement 6 minutes. Départs toutes les 10 à 20 minutes.\n"
            "- Navibus Loire Ligne N2 : Relie le 'Bas-Chantenay' au 'Hangar à Bananes' (pointe ouest de l'Île de Nantes).\n"
            "- Navibus Erdre : Liaison fluviale reliant Port-Boyer à Petit-Port / Facultés, très prisée des étudiants et promeneurs.\n"
            "C'est un moyen écologique, rapide et panoramique d'apprécier la ville depuis les flots."
        )
    },
    {
        "id": "transports_bicloo_velo",
        "category": "transports",
        "title": "Vélos en libre-service Bicloo et pistes cyclables",
        "keywords": ["velo", "bicloo", "bicyclette", "pistes cyclables", "location velo", "electrique", "mobilité douce"],
        "content": (
            "Nantes est l'une des villes les plus cyclables de France, dotée de plus de 500 km d'aménagements cyclables (dont la célèbre véloroute 'La Loire à Vélo').\n"
            "- Bicloo Plus : Réseau de vélos en libre-service avec plus de 120 stations et 1 200 vélos dans toute la métropole. "
            "Des formules courte durée (ticket 1 jour à 2€ ou 3 jours à 4€) sont disponibles directement aux bornes par carte bancaire ou sur l'application Bicloo. "
            "Les 30 premières minutes de chaque trajet sont systématiquement offertes.\n"
            "- Des vélos à assistance électrique (Monbicloo) et des abris vélo sécurisés sont également proposés par Naolib."
        )
    },
    {
        "id": "transports_aeroport",
        "category": "transports",
        "title": "Comment se rendre à l'Aéroport Nantes Atlantique (NTE)",
        "keywords": ["aeroport", "nantes atlantique", "avion", "navette aeroport", "terminal", "rejoindre aeroport", "gare sud"],
        "content": (
            "L'aéroport Nantes Atlantique (Bouguenais) se situe à 10 km au sud-ouest du centre-ville. Pour y accéder :\n"
            "1. La Navette Aéroport directe Naolib : Relie le hall d'arrivée de l'aéroport au centre de Nantes (Gare SNCF Sud et Cité des Congrès) en 20 minutes seulement. "
            "Fréquence : toutes les 20 minutes en semaine et toutes les 30 minutes le dimanche/jours fériés. Billet spécifique d'environ 10€, valable 3h sur l'ensemble du réseau de tram et bus.\n"
            "2. Option économique avec tickets urbains : Prendre le Tramway Ligne 3 jusqu'au terminus 'Neustrie', puis prendre le Bus 38 jusqu'à l'arrêt 'Aéroport' (coût : un simple ticket Naolib à 1,80€, gratuit le week-end).\n"
            "3. Taxi / VTC : Compter entre 25€ et 40€ selon l'heure pour une course vers le centre-ville."
        )
    },
    {
        "id": "transports_tarifs_titres",
        "category": "transports",
        "title": "Tarifs et tickets du réseau de transport Naolib (hors week-end)",
        "keywords": ["tarif", "tarifs", "prix", "ticket", "pass 24h", "acheter", "titre de transport", "valider"],
        "content": (
            "Du lundi au vendredi, les tarifs des titres de transport Naolib sont les suivants :\n"
            "- Ticket 1 heure : environ 1,80€ (valable 1h avec correspondances illimitées sur tram, busway, bus et navibus).\n"
            "- Carnet de 10 tickets 1 heure : environ 16,50€.\n"
            "- Pass 24h individuel : environ 6,40€ (trajets illimités pendant 24h sur tout le réseau urbain).\n"
            "- Pass 24h Famille / Multi-personnes : environ 12€ (valable pour un groupe de 1 à 4 personnes pendant 24h consécutives).\n"
            "- Rappel : LE WEEK-END (samedi et dimanche), tout le réseau urbain est 100% GRATUIT pour tous !\n"
            "Achat des titres : sur l'application mobile Naolib, aux distributeurs automatiques en station de tramway, ou par paiement sans contact par carte bancaire directement à bord."
        )
    },
    {
        "id": "transports_gare_sncf",
        "category": "transports",
        "title": "Gare SNCF de Nantes et accès",
        "keywords": ["gare", "sncf", "train", "tgv", "ter", "gare nord", "gare sud", "acces gare"],
        "content": (
            "La Gare de Nantes est une gare ferroviaire majeure avec deux accès reliés par une élégante mezzanine vitrée surplombant les voies :\n"
            "- Accès Nord : Donne sur le magnifique Jardin des Plantes et la station de Tramway Ligne 1 'Gare Nord' (liaison directe vers le Château, Commerce et les Chantiers Navals).\n"
            "- Accès Sud : Donne sur la Cité Internationale des Congrès, le pôle d'affaires Euronantes, la station Busway Ligne 5 et le départ de la Navette Aéroport express.\n"
            "Liaisons ferroviaires : TGV direct vers Paris Montparnasse en 2h00 à 2h10, liaisons directes vers Lyon, Lille, Marseille, Rennes et la côte Atlantique (Pornic, Le Croisic, Les Sables-d'Olonne)."
        )
    },

    # ==========================
    # LIEUX HISTORIQUES & TOURISME
    # ==========================
    {
        "id": "patrimoine_chateau_ducs",
        "category": "patrimoine",
        "title": "Château des ducs de Bretagne et Musée d'Histoire de Nantes",
        "keywords": ["chateau", "ducs de bretagne", "anne de bretagne", "remparts", "monument", "histoire", "forteresse", "visite"],
        "content": (
            "Le Château des ducs de Bretagne est le monument historique emblématique du cœur de Nantes. "
            "Édifié à la fin du XVe siècle par François II et sa fille Anne de Bretagne (deux fois reine de France), il s'agit d'une forteresse médiévale flanquée de puissants remparts et douves, "
            "abritant un somptueux palais résidentiel ducal de style Renaissance en pierre de tuffeau blanc.\n"
            "- Accès gratuit : La vaste cour intérieure, les douves paysagères et le chemin de ronde sur les remparts (500 mètres de promenade avec vue panoramique sur la ville) sont en ACCÈS LIBRE ET GRATUIT tous les jours (fermeture nocturne selon la saison).\n"
            "- Musée d'Histoire de Nantes : Aménagé dans les salles du logis ducal, il retrace l'histoire de la ville en 32 salles multimédias (la Bretagne ducale, la traite négrière et l'esclavage au XVIIIe siècle, la Révolution et les guerres de Vendée, la révolution industrielle et les célèbres biscuiteries LU).\n"
            "- Adresse : 4 place Marc Elder. Accès : Tram Ligne 1, station 'Duchesse Anne - Château'."
        )
    },
    {
        "id": "patrimoine_machines_ile",
        "category": "patrimoine",
        "title": "Les Machines de l'Île (Le Grand Éléphant & Carrousel des Mondes Marins)",
        "keywords": ["machines de l'ile", "elephant", "grand elephant", "carrousel", "mondes marins", "delaroziere", "jules verne", "chantiers navals"],
        "content": (
            "Les Machines de l'Île constituent un univers artistique et mécanique unique au monde, conçu par François Delaroziere et Pierre Orefice. "
            "Implantées sur le site des anciens chantiers navals de l'Île de Nantes, elles croisent l'imaginaire des voyages extraordinaires de Jules Verne (né à Nantes) et le génie mécanique de Léonard de Vinci.\n"
            "- Le Grand Éléphant : Véritable colosse mécanique de 12 mètres de haut, 48 tonnes d'acier et de bois sculpté. "
            "Il peut embarquer jusqu'à 50 passagers sur son dos pour une promenade spectaculaire sur les quais, barrit et projette de l'eau sur la foule amusée.\n"
            "- Le Carrousel des Mondes Marins : Gigantesque manège de 25 mètres de hauteur sur 3 niveaux superposés représentant les fonds sous-marins, peuplé de créatures aquatiques animées (calmar géant, crabe, poisson pirate, raie manta) que le public peut piloter. Il a été primé plus beau manège du monde.\n"
            "- La Galerie des Machines : Laboratoire vivant où les machinistes expliquent le fonctionnement des sculptures mécaniques et testent les futurs projets (comme l'Arbre aux Hérons).\n"
            "- Adresse : Boulevard Léon Bureau, Parc des Chantiers. Accès : Tram Ligne 1 (Chantiers Navals) ou Busway Ligne 5 (Prairie au Duc)."
        )
    },
    {
        "id": "patrimoine_passage_pommeraye",
        "category": "patrimoine",
        "title": "Le Passage Pommeraye (Galerie historique du XIXe siècle)",
        "keywords": ["passage pommeraye", "pommeraye", "galerie", "escalier", "commerce", "boutiques", "monument historique", "demy", "lola"],
        "content": (
            "Le Passage Pommeraye est un joyau architectural néoclassique unique en Europe, classé Monument Historique. "
            "Inauguré en 1843 par Louis Pommeraye, ce passage couvert relie la rue de la Fosse (en bas) à la rue Santeuil (en haut) en franchissant un dénivelé de plus de 9 mètres grâce à un somptueux escalier central monumental en bois et fonte orné de torchères et de statues allégoriques d'enfants représentant le Commerce, l'Industrie, l'Agriculture, les Beaux-Arts et les Sciences.\n"
            "- Ambiance : Éclairé par une monumentale verrière zénithale, il abrite d'élégantes boutiques, chocolateries, magasins de mode et cafés.\n"
            "- Cinéma : Lieu culte ayant servi de décor aux films de Jacques Demy (notamment 'Lola' et 'Une chambre en ville').\n"
            "- Accès : Entrée libre rue de la Fosse ou rue Santeuil. Arrêt de tram 1, 2 ou 3 à la station 'Commerce'."
        )
    },
    {
        "id": "patrimoine_jardin_des_plantes",
        "category": "patrimoine",
        "title": "Le Jardin des Plantes et le Palmarium",
        "keywords": ["jardin des plantes", "parc", "fleurs", "botanique", "camelia", "serres", "ponti", "gratuit", "nature"],
        "content": (
            "Situé en plein centre-ville, juste en face de la sortie Nord de la Gare SNCF, le Jardin des Plantes de Nantes s'étend sur plus de 7 hectares. "
            "Créé au début du XIXe siècle, il figure parmi les 4 plus importants jardins botaniques de France.\n"
            "- Points forts : Il abrite plus de 10 000 espèces végétales, dont une prestigieuse collection nationale de camélias (fleur symbole de Nantes), des magnolias centenaires et un séquoia géant.\n"
            "- Sculptures de Claude Ponti : Des créatures végétales géantes et poétiques inspirées des albums pour enfants de Claude Ponti (comme le célèbre 'Dormeur' géant en gazon ou les bancs démesurés) y amusent petits et grands.\n"
            "- Serres et Palmarium : Magnifiques serres historiques de l'époque Eiffel abritant une flore tropicale et équatoriale rare.\n"
            "- Détente : Bassins avec canards, volière, aires de jeux et l'agréable café-restaurant 'L'Orangerie' avec terrasse ombragée.\n"
            "- Entrée : Entièrement libre et gratuite tous les jours de l'année."
        )
    },
    {
        "id": "patrimoine_ile_versailles",
        "category": "patrimoine",
        "title": "L'Île de Versailles et son Jardin Japonais sur l'Erdre",
        "keywords": ["ile de versailles", "jardin japonais", "versailles", "erdre", "bateau electrique", "bambous", "zen"],
        "content": (
            "L'Île de Versailles est une île artificielle d'1,7 hectare située sur la rivière de l'Erdre, aménagée en un enchanteur jardin d'inspiration japonaise traditionnelle.\n"
            "- Décors : Cascades d'eau vive, rocailles de granit, ponts cintrés en bois rouge, bambouseraies, pins taillés en nuage, azalées et cerisiers du Japon.\n"
            "- La Maison de l'Erdre : Pavillon d'allure nippone au centre de l'île qui abrite des aquariums présentant les poissons d'eau douce de la rivière et des expositions thématiques.\n"
            "- Activités nautiques : Ponton de départ de bateaux électriques sans permis et canoës (Ruban Vert) pour naviguer tranquillement sur l'Erdre, bordée de manoirs et châteaux (qualifiée par François Ier de 'plus belle rivière de France').\n"
            "- Accès : Gratuit. Station de Tramway Ligne 2 'Motte-Rouge' ou 'Saint-Mihiel'."
        )
    },
    {
        "id": "patrimoine_cathedrale_saint_pierre",
        "category": "patrimoine",
        "title": "Cathédrale Saint-Pierre-et-Saint-Paul de Nantes",
        "keywords": ["cathedrale", "saint pierre", "eglise", "tombeau francois ii", "gothique", "patrimoine religieux"],
        "content": (
            "La Cathédrale Saint-Pierre-et-Saint-Paul est un chef-d'œuvre du style gothique flamboyant dont la construction s'est étalée sur plus de 450 ans (de 1434 à 1891). "
            "Ses voûtes de pierre blanche s'élèvent à 37,5 mètres de haut, soit davantage que celles de Notre-Dame de Paris.\n"
            "- Trésor national : Elle abrite le monumental tombeau en marbre blanc et noir de François II, dernier duc de Bretagne, et de son épouse Marguerite de Foix, sculpté au début du XVIe siècle par Michel Colombe à la demande de leur fille Anne de Bretagne.\n"
            "- Situation actuelle : Suite à l'incendie de juillet 2020 qui a détruit le grand orgue historique, la cathédrale fait l'objet d'un important chantier de restauration mené par l'État pour rouvrir progressivement au public."
        )
    },
    {
        "id": "patrimoine_voyage_nantes_ligne_verte",
        "category": "patrimoine",
        "title": "Le Voyage à Nantes (VAN) et le tracé de la Ligne Verte",
        "keywords": ["voyage a nantes", "ligne verte", "parcours", "art contemporain", "visiter", "circuit", "van"],
        "content": (
            "Le Voyage à Nantes est un concept touristique et culturel unique au monde : l'art contemporain s'expose dans l'espace public urbain toute l'année, avec un grand festival culturel chaque été.\n"
            "- La Ligne Verte : Un véritable tracé de peinture verte peint sur les trottoirs et rues de Nantes sur plus de 12 kilomètres. "
            "Il vous suffit de suivre cette ligne au sol pour ne rien manquer : elle relie tous les monuments phares (Château, Cathédrale, Théâtre Graslin, Passage Pommeraye), "
            "les œuvres d'art contemporaines pérennes disséminées dans la ville, les points de vue insolites et les parcs.\n"
            "- Gratuité : Suivre la ligne verte est totalement gratuit et constitue la meilleure manière de visiter Nantes à son propre rythme."
        )
    },
    {
        "id": "patrimoine_trentemoult",
        "category": "patrimoine",
        "title": "Le Village de Trentemoult (Rezé)",
        "keywords": ["trentemoult", "village", "reze", "pecheurs", "maisons colorees", "navibus", "guinguette", "bistrot"],
        "content": (
            "Trentemoult est un ancien village traditionnel de pêcheurs et capitaines cap-horniers situé sur la rive sud de la Loire, dans la commune de Rezé, en face de Nantes.\n"
            "- Charme et ambiance : Véritable dédale de ruelles piétonnes pavées, cours intérieures fleuries de palmiers et de glycines, façades de maisons peintes de couleurs vives (bleu, jaune, rouge ocre) qui servaient autrefois aux marins à utiliser les restes de peinture de leurs bateaux.\n"
            "- Sorties et gastronomie : Les quais de Trentemoult bordés de terrasses et guinguettes offrent une ambiance bohème idéale pour boire un verre au coucher du soleil face à la Loire.\n"
            "- Comment s'y rendre : Prendre le Navibus Ligne N1 depuis la Gare Maritime de Nantes (6 minutes de traversée, accessible avec un ticket urbain ou gratuit le week-end !)."
        )
    },
    {
        "id": "patrimoine_memorial_esclavage",
        "category": "patrimoine",
        "title": "Mémorial de l'abolition de l'esclavage",
        "keywords": ["memorial", "esclavage", "traite negriere", "abolition", "quai de la fosse", "histoire", "droits de l'homme"],
        "content": (
            "Nantes a été au XVIIIe siècle le premier port négrier de France, organisant plus de 1 800 expéditions de traite transatlantique. "
            "Aujourd'hui, la ville assume pleinement son passé et a érigé sur le quai de la Fosse l'un des plus grands mémoriaux au monde consacrés à la traite des Noirs et à l'abolition de l'esclavage, conçu par l'artiste Krzysztof Wodiczko et l'architecte Julian Bonder.\n"
            "- Parcours : Une esplanade paysagère le long de la Loire incrustée de 2 000 plaques de verre rappelant les navires négriers et les comptoirs, "
            "suivie d'un passage souterrain méditatif de 90 mètres sous les quais où sont gravés dans le verre des textes universels sur la liberté, la dignité et la lutte contre l'oppression.\n"
            "- Accès : Libre et gratuit tous les jours. Arrêt de tram 1 'Médiathèque' ou 'Chantiers Navals'."
        )
    },
    {
        "id": "patrimoine_tour_lu_lieu_unique",
        "category": "patrimoine",
        "title": "Le Lieu Unique et la Tour LU (Ancienne biscuiterie Lefèvre-Utile)",
        "keywords": ["lieu unique", "tour lu", "biscuiterie lu", "centre d'art", "spectacle", "hammam", "bar lu"],
        "content": (
            "Face au Château des ducs de Bretagne et au canal Saint-Félix, Le Lieu Unique occupe l'ancienne usine des célèbres biscuits LU (fondée en 1846 par Jean-Romain Lefèvre et Pauline-Isabelle Utile, inventeurs du Véritable Petit Beurre).\n"
            "- Architecture : Sa tour emblématique Art Nouveau aux couleurs bleu, blanc et or coiffée d'une renommée est l'un des symboles visuels de Nantes. On peut monter dans la tour pour admirer un panorama à 360° avec le 'Gyrorama'.\n"
            "- Scène nationale contemporaine : Reconverti en centre culturel avant-gardiste, Le Lieu Unique accueille des expositions d'art contemporain, spectacles de danse, concerts et festivals.\n"
            "- Lieux de vie : Grand bar convivial, restaurant, librairie spécialisée et un authentique hammam oriental traditionnel dans les sous-sols.\n"
            "- Accès : Quai Ferdinand-Favre. Tramway Ligne 1, arrêt 'Duchesse Anne - Château'."
        )
    },
    {
        "id": "patrimoine_musee_arts",
        "category": "patrimoine",
        "title": "Musée d'Arts de Nantes",
        "keywords": ["musee d'arts", "beaux arts", "peinture", "sculpture", "cube", "la tour", "monet", "kandinsky"],
        "content": (
            "Le Musée d'Arts de Nantes (rue Georges-Clemenceau) compte parmi les plus prestigieux musées de province de France. "
            "Rénové par le cabinet d'architectes britannique Stanton Williams, il relie majestueusement le Palais néoclassique du XIXe siècle, la Chapelle de l'Oratoire du XVIIe et 'Le Cube', bâtiment dédié à l'art contemporain.\n"
            "- Collections : Plus de 12 000 œuvres couvrant du XIIIe au XXIe siècle, avec des chefs-d'œuvre majeurs de Georges de La Tour ('Le Vielleur'), Rubens, Tintoret, Delacroix, Courbet, Claude Monet ('Les Nymphéas'), Vassily Kandinsky, Sonia Delaunay et Soulages.\n"
            "- Confort : Grand patio baigné de lumière naturelle, café restaurant, librairie et ateliers.\n"
            "- Accès : Tram 1 (Duchesse Anne ou Gare Nord) puis 5 min à pied."
        )
    },
    {
        "id": "patrimoine_hangar_bananes_buren",
        "category": "patrimoine",
        "title": "Le Hangar à Bananes et Les Anneaux de Buren",
        "keywords": ["hangar a bananes", "anneaux de buren", "daniel buren", "bar", "nuit", "restaurant", "quai des antilles", "ile de nantes"],
        "content": (
            "Situé à la pointe ouest de l'Île de Nantes, le Hangar à Bananes est un ancien entrepôt portuaire des années 1950 où mûrissaient les cargaisons de bananes venues de Guinée et des Antilles.\n"
            "- Réhabilitation festive : Il est devenu le haut lieu des sorties nantaises avec 8 000 m² de bars branchés, brasseries, terrasses avec vue directe sur la Loire, clubs musicaux et la galerie d'art contemporain 'HAB Galerie'.\n"
            "- Les Anneaux de Buren : Conçus par Daniel Buren et Patrick Bouchain pour la biennale Estuaire 2007, 18 anneaux métalliques monumentaux de 4 mètres de diamètre jalonnent le quai des Antilles. La nuit venue, ils s'illuminent en alternant anneaux rouges, verts et bleus, créant une perspective lumineuse féerique.\n"
            "- Accès : Busway Ligne 5 (terminus 'Hangar à Bananes') ou Navibus Ligne N2 depuis Bas-Chantenay."
        )
    },

    # ==========================
    # HÔTELS & HÉBERGEMENTS
    # ==========================
    {
        "id": "hotel_recommandations_quartiers",
        "category": "hotels",
        "title": "Où loger à Nantes : Recommandations par quartier",
        "keywords": ["hotel", "hotels", "dormir", "loger", "hebergement", "quartier", "ou loger", "centre", "gare", "ile de nantes"],
        "content": (
            "Pour choisir votre hébergement à Nantes selon votre type de séjour :\n"
            "1. Hypercentre / Graslin / Commerce / Bouffay : Le meilleur choix pour le tourisme à pied. Vous êtes au cœur des rues animées, des restaurants, du Passage Pommeraye et du Château. Idéal pour un week-end découverte.\n"
            "2. Gare SNCF / Cité des Congrès / Canal Saint-Félix : Très pratique pour les arrivées tardives en train, les salons professionnels ou les départs matinaux en navette aéroport. Quartier calme et à 10 min à pied du centre.\n"
            "3. Île de Nantes / Quartier de la Création : Ambiance moderne, créative et dynamique. À proximité immédiate des Machines de l'Île, de l'École de Design et des bars du Hangar à Bananes.\n"
            "4. Bords de l'Erdre / Saint-Mihiel : Atmosphère paisible, idéale pour les amateurs de balades au bord de l'eau."
        )
    },
    {
        "id": "hotel_haut_de_gamme_charme",
        "category": "hotels",
        "title": "Hôtels 4 étoiles et établissements de charme à Nantes",
        "keywords": ["hotel luxe", "hotel 4 etoiles", "sozo", "oceania", "radisson", "la perouse", "charme", "boutique hotel"],
        "content": (
            "Sélection des meilleurs hôtels de charme et haut de gamme à Nantes :\n"
            "- Sozo Hôtel (4 étoiles) : L'un des hôtels les plus insolites de France. Situé face au Jardin des Plantes (côté Gare Nord), il est aménagé au cœur d'une authentique chapelle du XIXe siècle réhabilitée. Chambres design sous des voûtes néo-gothiques de 17 mètres et vitraux d'origine.\n"
            "- Oceania Hôtel de France (4 étoiles) : Sur la prestigieuse place Graslin, face à l'Opéra. Ancien hôtel particulier du XVIIIe siècle où ont séjourné de nombreuses personnalités, doté d'un magnifique bar lounge sous verrière.\n"
            "- Hôtel La Pérouse (4 étoiles) : Situé entre la place Royale et la place du Cirque. Primé pour son architecture monolithique contemporaine penchée tout en pierre claire, chambres chaleureuses en bois naturel et petit-déjeuner composé de produits locaux du terroir nantais.\n"
            "- Maisons du Monde Hôtel & Suites (4 étoiles) : Rue Scribe (quartier Graslin). Décoration raffinée inspirée des univers de la célèbre marque d'ameublement, avec des suites spacieuses au confort haut de gamme.\n"
            "- Radisson Blu Hotel Nantes (4 étoiles) : Installé dans l'ancien Palais de Justice monumental de la place Aristide Briand. Hall majestueux avec colonnades néo-classiques et restaurant gastronomique."
        )
    },
    {
        "id": "hotel_milieu_gamme_affaires",
        "category": "hotels",
        "title": "Hôtels milieu de gamme et voyages d'affaires à Nantes (3 & 4 étoiles)",
        "keywords": ["hotel confort", "hotel affaires", "novotel", "mercure", "seven urban suites", "cite des congres", "appart-hotel"],
        "content": (
            "Pour un séjour confortable, familial ou professionnel :\n"
            "- Novotel Nantes Centre Bord de Loire (4 étoiles) : Situé sur les berges du fleuve, à seulement 5 minutes à pied de la Cité des Congrès et 10 minutes de la Gare Sud. Chambres modernes et vue sur l'eau.\n"
            "- Mercure Nantes Centre Grand Hôtel (4 étoiles) : En plein centre piétonnier (rue du Couëdic), parfait pour tout faire à pied.\n"
            "- Mercure Nantes Centre Gare (4 étoiles) : Directement accessible sur le parvis Sud de la gare et au pied du Busway ligne 5.\n"
            "- Seven Urban Suites (4 étoiles) : Sur l'Île de Nantes, appart'hôtel haut de gamme avec kitchenette équipée, spa/jacuzzi et parking sécurisé.\n"
            "- Okko Hotels Nantes Château (4 étoiles) : À deux pas du Château des ducs de Bretagne, concept tout compris contemporain avec 'Club' ouvert 24h/24 (apéritif généreux inclus le soir)."
        )
    },
    {
        "id": "hotel_economique_auberges",
        "category": "hotels",
        "title": "Hébergements économiques, petits budgets et auberges de jeunesse à Nantes",
        "keywords": ["hotel pas cher", "economique", "petit budget", "auberge de jeunesse", "manu", "hostel", "ibis", "b&b"],
        "content": (
            "Pour les voyageurs à petit budget, étudiants et routards :\n"
            "- Auberge de Jeunesse HI Nantes La Manu : Boulevard de Stalingrad (accessible en Tram Ligne 1, arrêt 'Manufacture'). "
            "Installée dans l'ancienne manufacture de tabacs rénovée. Propose des lits en dortoirs confortables et des chambres privées à prix très modiques, cuisine partagée, grand jardin et ambiance conviviale.\n"
            "- Ibis Styles Nantes Centre Place Royale (3 étoiles) : Hyper-central, décoration pop et petit-déjeuner buffet inclus dans le tarif de la nuitée.\n"
            "- B&B Hôtel Nantes Centre : Rue Paul Bellamy, chambres climatisées et insonorisées à prix très attractif, à 10 minutes à pied de la place du Cirque.\n"
            "- Résidences hôtelières Appart'City (Saint-Clément, Cité des Congrès, Viarme) : Studios avec cuisine pour faire des économies sur les repas."
        )
    },

    # ==========================
    # GASTRONOMIE & TERROIR
    # ==========================
    {
        "id": "gastronomie_specialites_nantaises",
        "category": "gastronomie",
        "title": "Spécialités culinaires et gourmandises nantaises",
        "keywords": ["specialites", "nourriture", "gateau nantais", "cure nantais", "muscadet", "berlingots", "rigolettes", "beurre blanc", "manger"],
        "content": (
            "Nantes possède une tradition gastronomique renommée, à la croisée de la Bretagne et de la vallée de la Loire :\n"
            "- Le Gâteau Nantais : La grande fierté sucrée locale ! Moelleux fondant à base d'amandes en poudre, d'œufs, de beurre et de farine, généreusement imbibé de rhum des Antilles et recouvert d'un glaçage blanc au sucre glace et rhum. Créé au XVIIIe siècle avec les denrées rapportées des îles par le port de Nantes.\n"
            "- Le Vin de Muscadet : Vin blanc sec AOC produit dans le vignoble nantais (AOP Muscadet Sèvre et Maine). Élevé sur lie, vif, iodé et perlant, c'est le compagnon indiscutable des huîtres bretonnes et vendéennes, ainsi que des poissons de Loire.\n"
            "- Le Fromage 'Le Curé Nantais' : Fromage au lait cru de vache à pâte molle et croûte lavée au Muscadet ou aux herbes, inventé à Saint-Julien-de-Concelles.\n"
            "- Le Beurre Blanc : Sauce créée par Clémence Lefeuvre au confluent de la Loire, émulsion onctueuse de beurre salé fondu, d'échalotes finement hachées et de réduction de vinaigre ou vin blanc, nappant traditionnellement un sandre ou un brochet de Loire.\n"
            "- Confiseries : Les Berlingots nantais (bonbons pyramidaux multicolores) et Les Rigolettes nantaises (coques de sucre craquantes fourrées d'une pulpe de fruit naturel : framboise, cassis, citron, mandarine)."
        )
    },
    {
        "id": "gastronomie_marches_adresses",
        "category": "gastronomie",
        "title": "Marchés et adresses gourmandes emblématiques à Nantes",
        "keywords": ["marche de talensac", "talensac", "la cigale", "bouffay", "restaurant", "bistrot", "creperie", "ou manger"],
        "content": (
            "Les hauts lieux de la gourmandise nantaise :\n"
            "- Le Marché de Talensac : Ouvert du mardi au dimanche matin (rue Talensac), c'est le plus grand et plus ancien marché couvert de la métropole. On y trouve le meilleur de la production locale : poissons frais de l'Atlantique, huîtres fraîches ouvertes sur place avec un verre de Muscadet, fromages affinés, charcuteries et galettes de blé noir toutes chaudes.\n"
            "- La Brasserie La Cigale : Située place Graslin, face à l'Opéra, inaugurée en 1895. Chef-d'œuvre du style Art Nouveau, ornée de somptueuses mosaïques, céramiques et faïences émaillées d'Émile Libaudière. Classée Monument Historique, on peut y déguster des plateaux de fruits de mer, poissons et le fameux gâteau nantais dans un cadre magique.\n"
            "- Le Quartier du Bouffay : Le cœur historique médiéval avec ses ruelles piétonnes bordées de crêperies bretonnes artisanales (dégustation de crêpes et galettes complètes accompagnées de cidre fermier), bars à vin et bistrots conviviaux."
        )
    },

    # ==========================
    # CONSEILS & ITINÉRAIRES
    # ==========================
    {
        "id": "pratique_itineraires_sejour",
        "category": "pratique",
        "title": "Itinéraires suggérés pour visiter Nantes (1 jour, 2 jours ou un week-end)",
        "keywords": ["visite 1 jour", "visite 2 jours", "programme", "circuit", "itineraire", "que faire", "incontournables"],
        "content": (
            "Suggestions d'itinéraires pour ne rien manquer :\n"
            "- En 1 jour (Les Essentiels) :\n"
            "  * Matin : Promenade dans la cour et sur les remparts du Château des ducs de Bretagne (gratuit) puis traversée du magnifique Jardin des Plantes.\n"
            "  * Déjeuner : Dans les ruelles du Bouffay ou sous les verrières de La Cigale.\n"
            "  * Après-midi : Traverser le Passage Pommeraye, puis se diriger vers les Machines de l'Île pour voir le Grand Éléphant en marche et le Carrousel des Mondes Marins.\n"
            "  * Fin d'après-midi : Prendre le Navibus à la Gare Maritime pour une traversée de 6 minutes vers Trentemoult et admirer le coucher de soleil en terrasse.\n\n"
            "- En 2 jours / Un week-end complet :\n"
            "  * Jour 1 : Le parcours ci-dessus en profitant de la GRATUITÉ totale des transports le week-end !\n"
            "  * Jour 2 : Matinée gourmande au Marché de Talensac, puis visite du Musée d'Arts de Nantes. L'après-midi, remonter l'Erdre en bateau électrique depuis l'Île de Versailles ou découvrir le Mémorial de l'abolition de l'esclavage et le Hangar à Bananes avec les Anneaux de Buren."
        )
    },
    {
        "id": "pratique_pass_nantes",
        "category": "pratique",
        "title": "Le Pass Nantes (Tarifs et avantages touristiques)",
        "keywords": ["pass nantes", "pass touristique", "reduction", "voyage a nantes pass", "musees gratuits"],
        "content": (
            "Le Pass Nantes (proposé par Le Voyage à Nantes) est un forfait touristique disponible en versions 24h, 48h, 72h ou 7 jours :\n"
            "- Avantages : Accès gratuit à plus de 30 sites et attractions incontournables (Musée d'Histoire du Château, Galerie des Machines de l'Île, Carrousel des Mondes Marins, Musée d'Arts, Musée Jules Verne, croisière fluviale sur l'Erdre ou la Loire, visites guidées de la ville).\n"
            "- Transports : Inclut l'accès illimité au réseau de transports en commun Naolib (tram, bus, navibus, et navette aéroport express incluse).\n"
            "- Astuce : Le week-end, les transports réguliers Naolib étant déjà gratuits pour tout le monde, le Pass Nantes reste particulièrement avantageux pour les entrées coupe-file dans les musées et attractions privées.\n"
            "- Où l'acheter : À l'Office de Tourisme (9 rue des États, face au Château) ou en ligne sur le site officiel de Nantes Tourisme."
        )
    }
]

def get_all_chunks():
    """Retourne la totalité des morceaux de connaissances."""
    return KNOWLEDGE_CHUNKS

def get_categories():
    """Retourne la liste des thématiques disponibles."""
    return [
        {"id": "transports", "label": "Transports & Mobilité", "icon": "train", "badge": "Naolib"},
        {"id": "patrimoine", "label": "Lieux Historiques & Culture", "icon": "landmark", "badge": "Culture"},
        {"id": "hotels", "label": "Hôtels & Logements", "icon": "bed", "badge": "Hébergement"},
        {"id": "gastronomie", "label": "Gastronomie & Terroir", "icon": "utensils", "badge": "Gourmand"},
        {"id": "pratique", "label": "Bons plans & Itinéraires", "icon": "map-pin", "badge": "Tourisme"}
    ]

