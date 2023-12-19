/* 
   Fazer copy-paste deste ficheiro
   para um terminal de SQL e executar.
*/

drop table if exists emp; /**/
drop table if exists dep;
drop table if exists descontos;
drop table if exists projecto;

/* Cria a tabela dos descontos
 */
CREATE TABLE descontos
(escalao      NUMERIC(2)      CONSTRAINT pk_esc_descontos PRIMARY KEY               ,
 salinf       NUMERIC(7)      CONSTRAINT nn_inf_descontos CHECK (salinf IS NOT NULL), 
 salsup       NUMERIC(7)      CONSTRAINT nn_sup_descontos CHECK (salsup IS NOT NULL)
);



/* Cria a tabela dos departamentos
 */
CREATE TABLE dep
(ndep         NUMERIC(2)      CONSTRAINT pk_ndep_dep      PRIMARY KEY               , 
 nome         VARCHAR(15)   CONSTRAINT nn_nome_dep      CHECK (nome   IS NOT NULL),
 local        VARCHAR(15)   CONSTRAINT nn_local_dep     CHECK (local  IS NOT NULL)
);



/* Cria a tabela dos empregados
 */
CREATE TABLE emp
(nemp          NUMERIC(4)      CONSTRAINT pk_nemp_emp     PRIMARY KEY, 
 nome          VARCHAR(20)   CONSTRAINT nn_nome_emp     NOT NULL   , 
 funcao        VARCHAR(12)   CONSTRAINT nn_funcao_emp   NOT NULL   , 
 encar         NUMERIC         CONSTRAINT fk_encar_emp 
                                 REFERENCES emp(nemp)    NULL       , 
 data_entrada  DATE           DEFAULT now()                        
                              CONSTRAINT nn_data_emp     NOT NULL   ,
 sal           NUMERIC(7)      CONSTRAINT nn_sal_emp      NOT NULL   ,
 premios       NUMERIC(7)      DEFAULT NULL                          , 
 ndep          NUMERIC(2)      CONSTRAINT nn_ndep_emp     NOT NULL 
                              CONSTRAINT fk_ndep_emp
                                 REFERENCES dep(ndep)
);

/* Cria a tabela de projecto
 */


CREATE TABLE projecto
(nprojecto          NUMERIC(7)      CONSTRAINT pk_nprojecto_projecto     PRIMARY KEY, 
 nome          VARCHAR(50)   CONSTRAINT nn_nome_projecto     NOT NULL   , 
 gestor         NUMERIC         CONSTRAINT fk_gestor_projecto 
                                 REFERENCES emp(nemp)    NULL       , 
 data_inicio  DATE           DEFAULT now()                        
                              CONSTRAINT nn_data_projecto     NOT NULL   ,
 data_fim  DATE,                                  
 cliente       VARCHAR(50)   CONSTRAINT nn_cliente_projecto     NOT NULL   ,
 ndep          NUMERIC(2)      CONSTRAINT nn_ndep_projecto     NOT NULL 
                              CONSTRAINT fk_ndep_projecto
                                 REFERENCES dep(ndep),
custo		NUMERIC(10),
valor		NUMERIC(10)
);


