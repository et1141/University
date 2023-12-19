insert into "brGuitars_luthier" (name, country, birth, death, pic)
values
('Antonio Tessarin', 'Brasil', null, null, 'https://www.violaobrasileiro.com.br/app/webroot/files/uploads/ckfinder/images/Tessarin%20Destaque.jpg'),
('Sérgio Abreu', 'Brasil', 1948, null, 'https://guitarcoop.com.br/gtc/wp-content/uploads/2016/01/sergio-abreu-guitarcoop-entrevista-1.jpg'),
('Will Hamm', 'Canada', null, null, 'https://hammstrings.com/wp-content/uploads/2015/04/Will-Hamm.jpg');


insert into "brGuitars_artist" (name, country, birth, death, pic)
values
('Ulisses Rocha', 'Brasil', 1960, null, 'https://img.discogs.com/z2q6ST1LdvB9Urv_UZG4mBlTxWM=/600x399/smart/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/A-399042-1441106248-4288.jpeg.jpg'),
('Daniel Murray', 'Brasil', 1981, null, 'http://www.kleberpatricio.com.br/wp-content/uploads/2019/04/dm-1024x683.jpg'),
('Yamandu Costa', 'Brasil', 1980, null, 'https://www.rbsdirect.com.br/imagesrc/25666109.jpg'),
('Paulo Bellinati', 'Brasil', 1950, null, 'http://www.guitarplayer.com.br/materias/1225.jpg'),
('Sebastião Tapajós', 'Brasil', 1943, 2021, 'https://s2.glbimg.com/zjsvHa83gl3o_JvUA_EaElWZuvg=/0x0:660x494/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2018/O/V/AzLMI0ROSMDgZg1pyd2Q/sebastiao-tapajos.jpg');

insert into "brGuitars_guitar" (luthier_id, model, year, top, bottom, sides, neck, fretboard, sadle, "tuningMachines")
values
((select id from "brGuitars_luthier" where name = 'Antonio Tessarin'), 'estudo', 2003, 'pinho alemão', 'jacarandá orelha de onça', 'jacarandá orelha de onça', 'cedro brasileiro', 'ébano indiano', 'jacarandá orelha de onça', 'Schaller'),
((select id from "brGuitars_luthier" where name = 'Antonio Tessarin'), 'concerto', 2007, 'abeto europeu', 'jacarandá bahia', 'jacarandá bahia', 'cedro brasileiro', 'ébano indiano', 'jacarandá bahia', 'Schaller'),
((select id from "brGuitars_luthier" where name = 'Sérgio Abreu'), 'concerto', null, 'abeto europeu', 'jacarandá bahia', 'jacarandá bahia', 'cedro brasileiro', 'ébano indiano', 'jacarandá bahia', 'Rubner'),
((select id from "brGuitars_luthier" where name = 'Will Hamm'), 'Yamandu Signature', null, 'cedro canadense', 'ébano macassar', 'ébano macassar', 'cedro canadense', 'ébano indiano', 'ébano macassar', 'custom hand made'),
((select id from "brGuitars_luthier" where name = 'Antonio Tessarin'), '10 cordas', null, 'abeto europeu', 'jacarandá bahia', 'jacarandá bahia', 'cedro brasileiro', 'ébano indiano', 'jacarandá bahia', 'Schaller');

insert into "brGuitars_guitarpic" (guitar_id, img)
values
((select g.id from "brGuitars_guitar" g, "brGuitars_luthier" l  where  l.id = g.luthier_id and g.model='Yamandu Signature' and l.name='Will Hamm'), 'https://hammstrings.com/wp-content/uploads/2015/06/yamandu-signature-hammstrings-1.jpg'),
((select g.id from "brGuitars_guitar" g, "brGuitars_luthier" l  where  l.id = g.luthier_id and g.model='Yamandu Signature' and l.name='Will Hamm'), 'https://hammstrings.com/wp-content/uploads/2015/06/yamandu-signature-hammstrings-2.jpg'),
((select g.id from "brGuitars_guitar" g, "brGuitars_luthier" l  where  l.id = g.luthier_id and g.model='estudo' and l.name='Antonio Tessarin'), 'https://http2.mlstatic.com/D_NQ_NP_827742-MLB46880924996_072021-W.jpg'),
((select g.id from "brGuitars_guitar" g, "brGuitars_luthier" l  where  l.id = g.luthier_id and g.model='concerto' and l.name = 'Antonio Tessarin'), 'https://http2.mlstatic.com/D_NQ_NP_900955-MLB28791439558_112018-W.jpg'),
((select g.id from "brGuitars_guitar" g, "brGuitars_luthier" l  where  l.id = g.luthier_id and g.model='concerto' and l.name = 'Sérgio Abreu'), 'http://bp3.blogger.com/_vtexxk1wb9c/SAtnz5hTZSI/AAAAAAAABSo/GDyeK_PnKds/s320/abreu_1990_front_hr.jpg'),
((select g.id from "brGuitars_guitar" g, "brGuitars_luthier" l  where  l.id = g.luthier_id and g.model='10 cordas' and l.name = 'Antonio Tessarin'), 'https://4.bp.blogspot.com/-Cv75yyeOEuk/W14jwqm4mSI/AAAAAAAAMCY/EXCy07dw3NY4U0kl6vQuMB662apPXGu_ACLcBGAs/s1600/daniel_murray_foto_gal_%2Bopido_gde%25281%2529.jpg');

insert into "brGuitars_recording" (artist_id, guitar_id, name, year, composer, arrangement, audio)
values
(
	(select id from "brGuitars_artist" where name='Paulo Bellinati'),
	(select g.id from "brGuitars_guitar" g, "brGuitars_luthier" l  where  l.id = g.luthier_id and g.model='concerto' and l.name = 'Sérgio Abreu'),
	'Jongo', 2000, 'Paulo Bellinati', null, 'https://www.youtube.com/embed/EWcTCg1q2aI'
),
(
	(select id from "brGuitars_artist" where name='Ulisses Rocha'),
	null, 'Rua Harmonia', 2010, 'Ulisses Rocha', null, 'https://www.youtube.com/embed/M-lAVOxOMNw'
),
(
	(select id from "brGuitars_artist" where name='Daniel Murray'),
	(select g.id from "brGuitars_guitar" g, "brGuitars_luthier" l  where  l.id = g.luthier_id and g.model='10 cordas' and l.name = 'Antonio Tessarin'),
	'Palhaço', 2016, 'Egberto Gismonti', 'Daniel Murray', 'https://www.youtube.com/embed/EDJFt_OsEGE'
),
(
	(select id from "brGuitars_artist" where name='Ulisses Rocha'),
	null, 'Adios Nonino', 2020, 'Astor Piazzolla', 'Cacho Tirao', 'https://www.youtube.com/embed/IIEM6Jlq_wc'
),
(
	(select id from "brGuitars_artist" where name='Yamandu Costa'),
	(select g.id from "brGuitars_guitar" g, "brGuitars_luthier" l  where  l.id = g.luthier_id and g.model='Yamandu Signature' and l.name = 'Will Hamm'),
	'Porro', 2018, 'Gentil Montana', 'Yamandu Costa', 'https://www.youtube.com/embed/EXeHPUMpM2U'
),
(
	(select id from "brGuitars_artist" where name='Sebastião Tapajós'),
	null, 'Carimbó', null, 'Sebastião Tapajós', null, 'https://www.youtube.com/embed/g8uy2Ziv7OE'
);
