word_list = ['abandonar', 'abominar', 'abril', 'aceite', 'acelga', 'acero', 'acordeón', 'acosar', 'acróstico',
             'acuarela', 'adrede', 'aduana', 'adulterio', 'afrodisíaco', 'agasajar', 'agenesia', 'agiotista',
             'agnosticismo', 'agosto', 'ahorrar', 'alabarda', 'alarma', 'alcancía', 'alegoría', 'alférez', 'alguacil',
             'aljamía', 'almanaque', 'almirante', 'ambrosía', 'amígdala', 'amortiguar', 'anaconda', 'anacronismo',
             'anfitrion', 'anfractuoso', 'anosognosia', 'antinomia', 'anzuelo', 'apostrofe', 'apostrofo', 'aquelarre',
             'aquilatar', 'arandela', 'arbitrario, ria', 'Argentina', 'ariete', 'arlequín', 'armario', 'arpa', 'arpía',
             'arsenal', 'artilugio', 'arzobispo', 'asesino', 'astrolabio', 'atlántico', 'auspicio', 'azud',
             'Babia, estar en', 'bacanal', 'Bahamas', 'baladí', 'bambalina', 'barbulla', 'bariatrico', 'barril',
             'barrica', 'bastardo', 'bayoneta', 'bergantín', 'biblia', 'bigote', 'biombo', 'bisiesto', 'bledo',
             'Brasil', 'broquel', 'bruma', 'bucólico', 'buhardilla', 'bujía', 'bulimia', 'burguesia', 'calendario',
             'calipigio, gia', 'calzar', 'camarón', 'cameo', 'camisa', 'camorra', 'camuflaje', 'can', 'cáñamo',
             'canario', 'candidato', 'capilla', 'carabina', 'carambola', 'cariátide', 'carillon', 'carnero', 'carótida',
             'carpetovetónico', 'carpintero', 'casa', 'catacresis', 'católico', 'celta', 'censor', 'ceremonia',
             'cháchara', 'chambergo', 'chic', 'chofer', 'chusma', 'cibernética', 'cilicio', 'cimiento', 'cimitarra',
             'circadiano', 'cirujano', 'clandestino', 'clérigo', 'cliente', 'clínica', 'clon', 'cloro', 'cobalto',
             'cobre', 'coche', 'cóctel', 'cofín', 'cólera', 'colon', 'colonia', 'comedia', 'comer', 'conde',
             'condestable', 'contradanza', 'convento', 'Copacabana', 'coqueto', 'cordobán', 'corona', 'correo',
             'cráter', 'criselefantino', 'crisis', 'cuatrero', 'cubierto', 'cucaracha', 'cultura', 'damajuana',
             'debacle', 'defenestrar', 'deliberar', 'democracia', 'demonio', 'deporte', 'derivar', 'desflorar',
             'detalle', 'detective', 'devoto, ta', 'diacrítico', 'dialelo', 'dicha', 'difteria', 'dilapidar',
             'dinamita', 'dinero', 'diploma', 'discrepar', 'dispepsia', 'dólar', 'doméstico', 'droga', 'druida', 'duda',
             'duelo', 'duende', 'duodeno', 'eclipse', 'economía', 'ecuador', 'edecán', 'edredón', 'electricidad',
             'elefante', 'elegante', 'elenco', 'elipse', 'elite', 'elixir', 'emoción', 'empatar', 'empatía',
             'emperifollado', 'encerrar', 'encomio', 'endriago', 'enero', 'enfurruñado', 'ensayo', 'entretenimiento',
             'entrevero', 'epanadiplosis', 'epidemia', 'epigrama', 'epónimo', 'equidna', 'eritrocito', 'esbirro',
             'escabroso', 'escafoides', 'escamotear', 'escaparate', 'escarlata', 'escatología', 'escorbuto',
             'esfenoides', 'esguince', 'esmalte', 'esplín', 'estafar', 'estantigua', 'estéril', 'estéril', 'estética',
             'estímulo', 'estoico', 'estraperlo', 'exorcismo', 'exótico', 'expedición', 'explicar', 'expreso',
             'exquisito', 'fabuloso', 'faquir', 'farsante', 'fascismo', 'favela', 'feijoada', 'fetiche', 'fettuccine',
             'fideo', 'filatelia', 'filología', 'fiscal', 'fisco', 'flamenco', 'flecha', 'foco', 'focal', 'folclore',
             'fornicar', 'foxtrot', 'franela', 'fuga', 'furia', 'gabinete', 'gaceta', 'gálibo', 'galicursi', 'gallo',
             'misa', 'gama', 'garaje', 'gastronomía', 'gazapo', 'gaznápiro', 'genética', 'genio', 'ingenio',
             'geografía', 'geranio', 'gnomo', 'gorila', 'góspel', 'gozo', 'granate', 'grito', 'grulla', 'guadaña',
             'guapo, pa', 'guarida', 'Guatemala', 'hábeas corpus', 'hamburguesa', 'harén', 'hebilla', 'helio', 'héroe',
             'herpes', 'hígado', 'himeneo', 'hipopótamo', 'hito', 'hocico', 'honor', 'humus', 'hurí', 'idilio',
             'ilusión', 'imán', 'imbécil', 'impresionismo', 'inaugurar', 'incólume', 'incunable', 'índigo',
             'inexorable', 'infancia', 'infarto', 'influenza', 'inmunidad', 'inocente', 'insigne', 'instinto',
             'intuición', 'investigar', 'Islas Malvinas', 'jabon', 'jamon', 'jaqueca', 'jardin', 'jinete',
             'jitanjáfora', 'jovial', 'judio', 'kiosco', 'laberinto', 'laca', 'ladrón', 'lagarto', 'larva', 'lechuga',
             'leitmotiv', 'lempira', 'letras', 'leyenda', 'libertinaje', 'Libia', 'libreto', 'liceo', 'limítrofe',
             'linchar', 'litera', 'llama', 'llorar', 'lona', 'lotería', 'lubricán', 'Lucifer', 'lujuria', 'luna',
             'luto', 'macadán', 'magenta', 'magnetismo', 'magnolia', 'maguey', 'majada', 'malandrín', 'Malvinas',
             'mambo', 'mandinga', 'manglar', 'mano', 'margarita', 'Maricastaña, el tiempo de', 'marioneta', 'mariscal',
             'marrano', 'mártir', 'marzo', 'máscara', 'masonería', 'matrícula', 'mazmorra', 'médico', 'melodía',
             'menaje', 'menú', 'meollo', 'mequetrefe', 'mercado', 'mercurio', 'merengue', 'merienda', 'metáfora',
             'meteoro', 'México', 'mientras', 'milonga', 'mimbre', 'mimo', 'miniatura', 'mismo', 'misterio', 'mitra',
             'mitridatismo', 'mojigato', 'mondongo', 'monzón', 'moretón', 'morfina', 'morganático', 'morgue', 'morlaco',
             'mormazo', 'mosquetero', 'mucama', 'muelle', 'mujer', 'museo', 'narcisismo', 'narval', 'Navidad', 'nazi',
             'nefasto', 'negacionismo', 'neurona', 'nicotina', 'nigromancia', 'nimio', 'nomeolvides', 'novela', 'nudo',
             'obedecer', 'oboe', 'obsceno', 'obús', 'océano', 'octubre', 'oficio', 'ogro', 'oleaginoso', 'olfato',
             'olvido', 'ombligo', 'ominoso', 'ónix', 'onomatopeya', 'opio', 'optimismo', 'oráculo', 'orangután', 'orín',
             'ornitorrinco', 'oropéndola', 'orquídea', 'ovación', 'página', 'pagoda', 'paladio', 'palurdo',
             'panegírico', 'panorama', 'pantalón', 'panteón', 'paralelo', 'paramecio', 'parangón', 'paranoia',
             'parásito', 'pariente', 'parquet', 'párroco', 'parsec', 'Pascua', 'pasteurización', 'patraña', 'pecuario',
             'pedazo', 'pegar', 'penacho', 'pera', 'perdiz', 'peregrino', 'período', 'peroné', 'perpetrar', 'petróleo',
             'piara', 'pícaro', 'pindárico', 'pineal', 'piquete', 'pirámide', 'pírrico', 'piscina', 'pista', 'pistón',
             'plagio', 'planeta', 'plástico', 'polimatía', 'pólipo', 'política', 'Polonia', 'pomada', 'pompa', 'ponche',
             'pontífice', 'pordiosero', 'postergar', 'potasio', 'prebenda', 'prebenda', 'presbítero', 'priapismo',
             'procrastinar', 'programa', 'proletario', 'propóleo', 'protocolo', 'proxeneta', 'psicología',
             'psicosomático', 'pterodáctilo', 'puerperio', 'pupitre', 'púrpura', 'quark', 'quintaesencia', 'radar',
             'radio', 'raíz', 'rambla', 'ramera', 'ramera', 'rapsodia', 'rebuznar', 'recalcitrante', 'recluso',
             'récord', 'refunfuñar', 'regalar', 'regañar', 'remoto', 'remuneración', 'reservar', 'resiliencia',
             'restaurante', 'retaliación', 'reticencia', 'rey', 'rezar', 'robar', 'robot', 'rococó', 'rosario',
             'rotisería', 'rúbrica', 'rueda', 'ruleta', 'rupestre', 'sagrado', 'sainete', 'salario', 'sándwich',
             'santabárbara', 'sarao', 'sarcasmo', 'sartorio', 'satélite', 'seguridad', 'semántica', 'septiembre', 'ser',
             'seudónimo', 'sexagesimal', 'sibarita', 'sífilis', 'silencio', 'siniestro', 'sodomía', 'sofisticado',
             'sofocar', 'somático', 'sororidad', 'sota', 'taberna', 'tafetán', 'tahona', 'talento', 'tándem', 'tañer',
             'tartufo', 'tatuaje', 'taxidermia', 'taxímetro', 'testarudo', 'tifón', 'tilo', 'tímpano', 'tinnitus',
             'tiovivo', 'tirabuzón', 'titán', 'toalla', 'tomate', 'toronja', 'tos ferina o convulsa', 'tramoya',
             'trapecio', 'tregua', 'triaje', 'tribu', 'tripa', 'triunfo', 'troglodita', 'ufanar', 'ultracorrección',
             'utopía', 'vacuna', 'vasallo', 'vaselina', 'vedete', 'veneno', 'verbena', 'vereda', 'veronal', 'veto',
             'viático', 'vicario', 'victoria', 'vino', 'violeta', 'violín', 'virus', 'vitamina', 'vitolfilia',
             'vituperar', 'viuda', 'vocación', 'vodevil', 'vudú', 'whisky', 'yanqui', 'yate', 'yelmo', 'yugular',
             'zafarrancho', 'zahón', 'zanahoria', 'zar', 'zonzo']
