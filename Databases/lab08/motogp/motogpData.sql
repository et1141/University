insert into "brMotogp_team" (name, country, pic)
values
('Ducati', 'Brasil', 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Ducati_MotoGP_04_%2810760413416%29.jpg'),
('Aprillia', 'Brasil', 'https://upload.wikimedia.org/wikipedia/commons/0/06/Aleix_Espargar%C3%B3_leads_the_pack_2021_Sachsenring_%28cropped%29.jpg'),
('KTM', 'Canada', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/KTM_MotoGP_Bike_RC16.jpg/1024px-KTM_MotoGP_Bike_RC16.jpg');


insert into "brMotogp_driver" (name, country, birth, death, pic)
values
('Ulisses Rocha', 'Brasil', 1960, null, 'https://img.discogs.com/z2q6ST1LdvB9Urv_UZG4mBlTxWM=/600x399/smart/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/A-399042-1441106248-4288.jpeg.jpg'),
('Daniel Murray', 'Brasil', 1981, null, 'http://www.kleberpatricio.com.br/wp-content/uploads/2019/04/dm-1024x683.jpg'),
('Yamandu Costa', 'Brasil', 1980, null, 'https://www.rbsdirect.com.br/imagesrc/25666109.jpg'),
('Paulo Bellinati', 'Brasil', 1950, null, 'http://www.guitarplayer.com.br/materias/1225.jpg'),
('Sebastião Tapajós', 'Brasil', 1943, 2021, 'https://s2.glbimg.com/zjsvHa83gl3o_JvUA_EaElWZuvg=/0x0:660x494/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2018/O/V/AzLMI0ROSMDgZg1pyd2Q/sebastiao-tapajos.jpg');

insert into "brMotogp_moto" (team_id, model, brand,size,cc,hp)
values
((select id from "brMotogp_team" where name = 'Ducati'), 'D1', 'Ducati',2,1000,150),
((select id from "brMotogp_team" where name = 'Ducati'), 'D2', 'Ducati',2,1000,150),
((select id from "brMotogp_team" where name = 'Aprillia'), 'A1', 'Aprillia',2,1100,155),
((select id from "brMotogp_team" where name = 'KTM'), 'K1', 'KTM',2,1200,160);

insert into "brMotogp_motopic" (moto_id, img)
values
((select id from "brMotogp_moto" m where m.model='D1'), 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Ducati_MotoGP_04_%2810760413416%29.jpg'),
((select id from "brMotogp_moto" m where m.model='D2'), 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Ducati_MotoGP_04_%2810760413416%29.jpg'),
((select id from "brMotogp_moto" m where m.model='A1'), 'https://upload.wikimedia.org/wikipedia/commons/0/06/Aleix_Espargar%C3%B3_leads_the_pack_2021_Sachsenring_%28cropped%29.jpg'),
((select id from "brMotogp_moto" m where m.model='K1'), 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/KTM_MotoGP_Bike_RC16.jpg/1024px-KTM_MotoGP_Bike_RC16.jpg');

insert into "brMotogp_drives" (driver_id, moto_id, dateSTART, dateEND)
values
(
	(select id from "brMotogp_driver" where name='Ulisses Rocha'),
	(select id from "brMotogp_moto" m where m.model='D1'),
	2020,2021
);
