# this program extracts phone numbers and email from content provided
# written by xinyu
import re

text = r'''EXAMPLE PHONE AND EMAIL
DIRECTORY
This example PDF was created to practice writing programs that could automatically get phone numbers
and email addresses from PDFs.
You can learn to program with the free resources at https://inventwithpython.com
PUBLIC DOMAIN IMAGE OF THE SEAL OF APPROVAL
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum."
Jessie Mckay jmckay67@aol.com 479-205-4874
Tom Jordan tjordan@msn.com 678-560-3485
Clayton Cross ccross20@gmail.com 724-900-2986
Rayford Sutton rayfords66@hotmail.com 242-391-3183
Jerome Gentry jgentry@me.com 604-720-6426
Weldon Camacho wcamacho57@icloud.com 651-807-8065
Quinton Franks qfranks@comcast.net 209-754-9111
Adam Hubbard cygzfjd61@outlook.com 641-433-6698
Jarred Fox jfox39@live.com 701-528-9851
Arnoldo Parker aparker39@sbcglobal.net 304-491-9583
Sid Mcdaniel mcdanie3354@att.net 863-583-8107
Raymon Combs uqcwsntti71@att.net 507-948-3980
Ervin Francis efrancis@optonline.net 546-367-3454
Gilberto Austin austi363@optonline.net 321-854-5616
Lino Barlow lbarlow22@me.com 904-896-2920
Stacey Shepherd sshepherd61@sbcglobal.net 309-387-1990
Roscoe Terry rterry64@outlook.com 605-373-2329
Eddie Meadows eddiem89@yahoo.com 573-454-1209
Carlos Simpson csimpson8@verizon.net 252-822-2439
Jerome Manning jmanning54@optonline.net 586-481-1805
Hong Erickson herickson3@me.com 615-716-5379
Burt Graham bgraham70@sbcglobal.net 903-995-3368
Mario Sloan msloan55@verizon.net 205-868-3935
Jeffry Mcintosh jmcintosh@icloud.com 881-376-2173
Owen Malone owenm64@yahoo.com 936-631-8841
Jamar Gilbert uzkp@yahoo.com 307-368-4710
Guadalupe Ramsey gramsey51@optonline.net 631-957-9402
Chet Ramsey cramsey91@outlook.com 336-402-2815
Lester Finch lfinch@gmail.com 511-768-9073
Mason Marquez masonm44@att.net 862-579-2515
Olen Boyer oboyer8@icloud.com 678-439-5117
Sherman Gamble tnjdmbnizb@comcast.net 949-328-4768
Gerry Mccarthy gmccarthy4@msn.com 764-582-6489
Jon Jefferson tzb23@yahoo.com 662-882-4349
Cristopher Maddox cmaddox@yahoo.com 323-686-4356
Abel Talley talle6@att.net 321-641-1192
Jerrod Hurst jhurst88@outlook.com 980-511-2211
Ezra Pickett epickett85@msn.com 931-381-2749
Delbert Mcintyre dmcintyre@optonline.net 557-314-1719
Tom Wilkins twilkins7@icloud.com 641-845-9700
Deandre Schneider deandres56@outlook.com 571-248-3160
Louie Gross lgross@me.com 611-848-3013
Cary Mathews cmathews23@verizon.net 724-392-9051
Clinton Hernandez chernandez16@yahoo.com 303-606-9242
Sylvester
Goodman sylvesterg@comcast.net 419-691-5429
Efren Daniels edaniels@comcast.net 740-228-1291
Myles Knapp mknapp26@outlook.com 479-529-9642
Trey Hendrix thendrix@me.com 308-702-9334
Gerardo Gonzales ggonzales@hotmail.com 704-481-3176
Collin Wilkinson cwilkinson7@comcast.net 270-245-5606
Hubert Moore hmoore12@yahoo.com 559-639-2831
Rudolph Joyce joyc5185@sbcglobal.net 506-203-1818
Raymundo Griffin rgriffin45@optonline.net 716-387-4756
Stanton Burris sburris@comcast.net 501-919-6026
Newton Huff nhuff@att.net 351-796-1964
Lonnie Gibson lgibson51@comcast.net 809-948-1893
Newton Mendez nmendez@mac.com 984-578-4176
Dominic Kane dkane93@msn.com 765-298-6852
Rey Alvarado alvarad24@live.com 309-531-8927
Maxwell Pittman mpittman9@gmail.com 561-405-2390
Freddy Nolan fnolan38@verizon.net 423-694-1512
Quentin Kane qkane60@me.com 561-365-7342
Marcelo Owens mowens88@aol.com 717-616-6054
Saul Warner swarner@mac.com 517-593-3243
Giuseppe Edwards gedwards@aol.com 971-374-3441
Glen Duffy gduffy35@optonline.net 313-758-7914
Johnson Bird cwnzm@hotmail.com 713-418-9707
Lon Mays lmays@gmail.com 811-557-8092
Orval Jones xugizlf81@live.com 601-247-7920
Stefan Wiley swiley19@sbcglobal.net 405-866-8158
Dewayne Vincent dvincent@verizon.net 940-998-9912
Elmo Morton emorton5@hotmail.com 904-383-5407
Trenton Randolph trentonr64@comcast.net 772-773-7846
Alonzo Noble alonzon17@aol.com 312-773-6768
Stephan Callahan scallahan89@optonline.net 814-960-3437
Merrill Morin mmorin73@mac.com 703-767-4323
Antonia Vasquez vasque3298@comcast.net 403-212-2346
Jerrod Horne jerrodh62@comcast.net 805-997-2016
Sammie Blanchard sblanchard44@att.net 415-595-9796
Renaldo Nielsen renaldon@comcast.net 252-739-5595
Rick Logan rlogan97@optonline.net 473-406-4822
Xavier Sexton ysbmcsipr3@comcast.net 778-569-3862
Delmer Chambers dchambers18@sbcglobal.net 410-418-7216
Melvin Dixon mdixon95@me.com 816-614-7357
Randell Wright rwright@att.net 307-476-5699
Kasey Mcbride mcbrid17@gmail.com 939-537-1879
Long Cohen cohe1696@yahoo.com 905-523-5311
Hunter Walton hwalton3@hotmail.com 975-675-8521
Jacques Dean jacquesd@att.net 515-420-4722
Nicky Cleveland ncleveland88@mac.com 573-286-5790
Heath Reeves hreeves56@mac.com 646-934-6224
Dannie Castro dcastro91@mac.com 473-909-5259
Malcolm Pickett picket8286@gmail.com 425-691-6076
Emil Bryant ebryant28@hotmail.com 740-912-1584
Lonny Trevino ltrevino@live.com 361-423-3274
Lamont Booker lbooker16@me.com 939-725-1384
Norberto Ramsey ramse3653@verizon.net 484-326-9103
Donny Mcintosh donnym24@live.com 207-389-7224
Antwan Harmon aharmon99@sbcglobal.net 947-684-9146
Cristopher
Blanchard cblanchard@msn.com 877-503-6944
Zane Glover zglover61@yahoo.com 601-896-4565
Ralph Booth rbooth23@mac.com 254-945-4889
Curtis Maddox curtism@verizon.net 417-576-2133
Deon David ddavid37@sbcglobal.net 627-632-6773
Salvador Short qxu@msn.com 812-983-9748
Curtis Rios crios28@yahoo.com 303-568-6327
Ashley William awilliam86@sbcglobal.net 402-497-9729
Nicholas Blanchard blanchar7913@icloud.com 441-769-3433
Jermaine
Stephenson jstephenson53@live.com 641-409-6385
Aubrey Knapp aubreyk90@msn.com 514-637-7967
Abel Shields abels@verizon.net 813-213-1319
Micheal Whitfield pmorp6@msn.com 704-231-9162
Royal Williams royalw65@verizon.net 229-718-3131
Hayden Barber hbarber66@sbcglobal.net 518-483-3634
Cruz Gregory cgregory@mac.com 231-296-9140
Stacy Wyatt wyat97@gmail.com 706-899-3971
Adrian Mason maso5913@gmail.com 464-525-8598
Faustino Sosa fsosa33@sbcglobal.net 464-999-6721
Toney Mccarty mccart6795@me.com 760-690-7194
Bill Gentry gentr9578@verizon.net 424-442-9011
Wallace Bullock wbullock50@hotmail.com 211-937-9457
Damon Blake dblake74@sbcglobal.net 234-238-8851
Waldo Castaneda wcastaneda@sbcglobal.net 904-838-7421
Wilford Yates wyates@att.net 320-944-8986
Chas Hicks hexxuxu97@icloud.com 881-674-8231
Miles Combs mcombs2@icloud.com 847-833-3195
Greg Goodwin goodwi99@sbcglobal.net 504-925-2032
Howard Palmer palme7345@live.com 984-739-5933
Teddy Underwood teddyu49@live.com 832-295-6774
Lanny Anthony dxa18@optonline.net 405-807-2836
Modesto Haley mhaley24@sbcglobal.net 559-710-6677
Dirk Watkins dwatkins@msn.com 903-628-5508
Fausto Quinn fquinn63@icloud.com 339-741-4816
Pablo Nguyen pablon88@aol.com 509-213-3802
Wayne Scott wscott@yahoo.com 608-743-7298
Christoper
Guerrero guerrer5579@comcast.net 843-618-3895
Joe Clay dhuy50@mac.com 307-922-7850
Riley Berry rberry36@outlook.com 703-663-5402
Casey Rosa ros81@msn.com 513-264-5926
Cleo Carver ccarver63@yahoo.com 239-856-1769
Eli Avery eavery@msn.com 718-379-7684
Percy Mathis percym86@yahoo.com 224-699-9948
Dante Briggs dbriggs68@att.net 727-437-8571
Robbie Spears uyqcq84@msn.com 240-841-7589
Galen Solis gsolis80@gmail.com 913-851-9474
Vince Mcdonald vmcdonald22@aol.com 270-796-8192
Alberto Hamilton ahamilton74@yahoo.com 418-393-3324
Dana Garner dgarner@gmail.com 815-834-1689
Martin Blackburn mblackburn48@me.com 218-986-7343
Rolland Graves rgraves8@optonline.net 585-227-9385
Jack Fulton jfulton61@live.com 806-463-3328
Glenn Logan loga4146@verizon.net 700-911-8905
Chung Hanson cpnxn91@att.net 308-973-7318
Korey Petersen kpetersen80@gmail.com 859-328-2032
Daniel Buckner dbuckner@outlook.com 859-301-4839
Eli Nicholson elin47@msn.com 216-207-9704
Timothy Alvarez xzwkvrg72@mac.com 631-926-6045
Rich Scott lflmzbbzh@optonline.net 867-402-4652
Long Morrison lmorrison36@yahoo.com 239-805-3865
Ernesto Deleon edeleon77@comcast.net 402-619-6555
King Mcgowan kmcgowan@comcast.net 877-623-7118
Tyron White twhite89@gmail.com 351-562-7333
Oscar Cash oscarc94@hotmail.com 361-447-2150
Darin Kelly dkelly@outlook.com 860-946-8955
Harry Bird bir8097@me.com 218-585-4289
Clyde Gillespie clydeg32@optonline.net 352-464-2633
Reynaldo Small rsmall61@gmail.com 270-618-4131
Damien Hatfield dhatfield30@icloud.com 845-511-8104
Cyril Wynn cwynn63@outlook.com 405-918-3937
Sidney Lara sidneyl@hotmail.com 464-390-2264
Pasquale Larson larso56@msn.com 242-726-1488
Olen Fuentes ofuentes67@verizon.net 662-743-9060
Floyd Bray tins28@gmail.com 209-732-1588
Dennis Fowler dfowler@me.com 239-519-8768
Hoyt Nielsen hnielsen88@yahoo.com 847-950-8510
Humberto Leonard leonar8259@live.com 412-975-6397
Sylvester
Maldonado smaldonado58@att.net 239-551-4133
Landon Goff lgoff67@comcast.net 900-442-1979
Ian Hebert heber22@hotmail.com 386-249-3186
Levi Oconnor loconnor93@att.net 880-553-1551
Theo Lloyd tlloyd@hotmail.com 767-978-1382
Britt Baird bbaird@gmail.com 336-660-3178
Luciano Donaldson omykcnmh8@verizon.net 313-778-4612
Larry Cummings larryc97@optonline.net 618-745-4805
Colin Bender cbender89@verizon.net 264-514-9602
Jae Davis jdavis49@msn.com 913-873-4406
Clark Alvarez yaehophxlt43@aol.com 580-711-6719
German Parsons parson87@me.com 307-897-7205
Lupe Conrad lconrad54@live.com 778-511-8803
Brendan Conley fcocztufbo79@comcast.net 737-888-4741
Cletus Bauer cbauer35@verizon.net 709-765-4993
Hilario Trevino htrevino47@sbcglobal.net 540-930-7062
Frances Clark fclark82@att.net 916-842-3938
Young Hernandez hernande713@verizon.net 402-505-7515
Trenton Robinson zlcqlnt21@comcast.net 917-530-7084
Monroe Winters mwinters94@me.com 516-501-5869
Rick Trevino rtrevino26@optonline.net 601-538-7861
Erwin Downs edowns@hotmail.com 660-268-3286
Margarito West wes6448@live.com 260-599-6493
Emmitt Quinn emmittq21@aol.com 541-359-8699
Vern Rodriguez vrodriguez@aol.com 316-362-3876
Ross Gutierrez rgutierrez37@msn.com 484-238-6979
Junior Fields jfields98@icloud.com 464-562-2555
Roman Baldwin rbaldwin28@msn.com 939-673-2435
Seymour Morton smorton58@verizon.net 612-241-8285
Franklin Lamb flamb51@live.com 246-914-9884
Bill Mccray bmccray14@yahoo.com 561-545-9594
Micah Murray murra7344@comcast.net 902-346-5892
Angelo Mckenzie amckenzie@optonline.net 517-879-4678
Son Atkinson satkinson56@mac.com 833-227-6959
Justin Perry gahu14@live.com 970-964-7403
Ron Mccoy rmccoy55@outlook.com 509-871-3552
Wallace Robertson wallacer81@yahoo.com 626-611-3619
Bertram Vega bvega39@yahoo.com 971-972-1597
Roscoe Hines kyxdmsnoh81@verizon.net 719-841-7163
Ismael Lewis ilewis38@aol.com 619-346-4110
Kurt Dunlap kurtd@mac.com 508-602-5051
Jimmy Valenzuela jvalenzuela12@optonline.net 727-615-7434
Willian Downs wdowns@att.net 828-375-9162
Grady Shaw gshaw98@yahoo.com 385-795-4623
Scottie Atkinson satkinson47@att.net 822-584-4566
Berry Phillips bphillips57@outlook.com 877-241-8837
Ian Graham igraham47@verizon.net 718-474-8986
Allen Clemons qbmgk@live.com 758-521-6779
Kirby Gilliam kgilliam@sbcglobal.net 231-830-4298
Evan Terry eterry67@yahoo.com 752-276-6713
Franklin Solomon fsolomon81@outlook.com 937-522-5976
Leonardo Barber barbe138@yahoo.com 564-854-2757
Connie Vincent cvincent38@hotmail.com 980-613-5291
Evan Richmond erichmond@live.com 765-235-1022
Myles Woodard mwoodard34@icloud.com 562-742-4234
Adan Armstrong aarmstrong39@att.net 872-336-6099
Samual Dorsey dorse4380@optonline.net 281-237-5202
Jules Merritt julesm60@verizon.net 334-551-4961
Shad Meyers smeyers78@sbcglobal.net 806-574-2800
Hosea Howell hhowell6@outlook.com 848-750-3377
Ward Clarke wclarke49@me.com 600-394-1825
Bennett Mckenzie bmckenzie49@aol.com 878-259-8254
Herschel Irwin herscheli@live.com 740-662-9378
Max Howe mhowe28@msn.com 904-372-9568
Carol Boyle cboyle11@hotmail.com 518-502-8801
Marc Daniels mdaniels@yahoo.com 646-279-2565
Lester Mcfarland lmcfarland7@hotmail.com 718-639-4360
Boris Bowers bbowers53@mac.com 810-209-6214
Lou Joyce louj89@msn.com 516-268-8591
Jermaine Love jlove99@gmail.com 414-460-6215
Antone Parsons tdymy79@live.com 511-359-9922
Xavier Everett xeverett92@verizon.net 313-337-4929
Francis Sheppard fsheppard@live.com 808-252-4393
Vicente Waller vwaller57@live.com 985-747-2466
Jerrell Sweet jsweet91@me.com 557-385-4600
Bo Ware bware30@gmail.com 561-887-6946
Ike Walsh iwalsh76@verizon.net 251-908-7682
Thomas Ford kppilspnbx1@live.com 805-324-5310
Spencer Mccarty smccarty19@outlook.com 509-735-5037
Anton Zimmerman antonz@icloud.com 479-370-6824
Jeffry Jacobson jjacobson@sbcglobal.net 517-610-2685
Joaquin Merrill jmerrill@aol.com 601-571-9567
Waylon Holder wholder34@me.com 811-230-2024
Federico Pickett yiafpwdr98@aol.com 800-514-7080
Milo Harper mharper@aol.com 615-208-3677
Andy Owen owe3619@comcast.net 957-802-8298
Kendall Mcmillan kmcmillan11@gmail.com 649-808-2639
Cortez Underwood cunderwood10@att.net 641-800-1884
Robin Michael rmichael63@live.com 284-474-5209
Orville Wade rfdct61@msn.com 336-422-7446
Pete Becker pbecker9@verizon.net 211-825-1882
Edwin Wilkerson ewilkerson41@icloud.com 857-975-5724
Fabian Fisher ffisher98@gmail.com 802-417-3513
Refugio Roth ozcir22@mac.com 315-699-1661
Millard Stewart mstewart95@outlook.com 802-231-2555
Odell Bailey baile513@msn.com 516-566-2494
Gayle Curry aigkbtdmnq@att.net 811-752-7869
Hilario Barr hbarr28@gmail.com 512-355-5025
Burt Finley burtf31@yahoo.com 710-478-3968
Teddy Randolph teddyr78@att.net 473-379-1236
Clarence Calhoun ccalhoun@live.com 911-939-5787
Waldo Rasmussen wrasmussen@mac.com 619-864-2272
Theo Kirk kir6754@verizon.net 702-520-2633
Hunter Cochran hcochran@outlook.com 972-237-5021
Herbert Meyer hmeyer29@me.com 435-270-1776
Aubrey Hudson aubreyh@live.com 957-844-5572
Cory Ramos cramos56@sbcglobal.net 345-325-5854
Merlin Hunter mhunter@aol.com 857-799-1123
Santiago Fuentes sfuentes@outlook.com 423-972-1868
Donny Mcintyre donnym84@me.com 732-512-2111
Armando Keith keit55@mac.com 303-324-8947
Cody Spears cspears@live.com 337-289-6754
Genaro Valdez gvaldez52@verizon.net 201-549-6070
Anibal Charles acharles53@live.com 811-663-1391
Aurelio Coffey coffe5429@hotmail.com 231-306-7737
Faustino Bishop fbishop@gmail.com 877-683-2440
Jerrell Morales jmorales87@mac.com 317-977-9813
Jonas Chang jonasc32@me.com 321-942-6841
Darrin Peters peter4280@icloud.com 590-892-9217
Kim Hooper hoope8340@icloud.com 805-838-5008
Shirley Carrillo shirleyc43@gmail.com 862-903-5577
Anderson Gibson agibson78@gmail.com 971-459-6814
Millard Foster millardf16@gmail.com 832-973-8787
Stephen Workman sworkman10@mac.com 724-235-8718
Rex Gonzalez rgonzalez19@yahoo.com 401-388-1482
Loyd Morris lmorris@icloud.com 620-456-6406
Alonzo Mckee amckee52@hotmail.com 604-970-5352
Aron Wise awise70@outlook.com 205-650-8301
Shelby Pope spope39@hotmail.com 503-692-6921
Robby Riggs tqqfpjflk38@comcast.net 832-401-6373
Tyron Cooper lsdjhcpu86@hotmail.com 627-940-2958
Domingo
Carpenter dcarpenter50@sbcglobal.net 412-988-2153
Walker Castro wcastro99@hotmail.com 702-441-4902
Elliot Goodwin egoodwin13@verizon.net 660-228-3120
Elliott Garcia egarcia36@outlook.com 970-346-7317
Cedrick May cmay@icloud.com 900-515-8022
Zack Golden zackg45@icloud.com 412-274-5147
Dannie Young dyoung42@me.com 811-671-7274
Ned Hansen nhansen69@live.com 844-981-7131
Bennett Andrews bandrews32@msn.com 928-363-1271
Jacques Golden jgolden18@yahoo.com 928-648-5234
Larry Hickman lhickman@verizon.net 607-685-6515
Jayson Aguirre jaguirre9@outlook.com 845-732-8332
Hugo Haney hhaney26@live.com 671-685-2562
Isidro Slater mudcejrd85@verizon.net 517-354-9683
Chas Wolfe chasw@gmail.com 585-457-1628
Coleman Duncan cduncan85@hotmail.com 415-651-9418
Augustine Burton aburton57@optonline.net 910-892-9556
Terrence Wooten jusdkxph@gmail.com 678-559-8557
Odis George dbbzbwb91@optonline.net 716-725-1472
Cory Bruce cbruce4@live.com 306-223-8164
Willard Koch vgblyq10@optonline.net 268-361-9914
Winford Norton wnorton23@hotmail.com 975-333-6787
Rubin Alston rubina87@hotmail.com 928-890-6926
Dino Skinner dskinner51@live.com 626-879-6822
Grady Clarke gclarke91@outlook.com 207-211-9430
Trevor Murray tmurray74@me.com 843-386-9067
Chase Macias cmacias98@sbcglobal.net 260-456-3631
Shad Ayers ayer7122@icloud.com 216-779-2942
Domenic Wise dwise43@msn.com 360-527-4014
Cory Combs ccombs32@outlook.com 207-490-9134
Brooks Lang blang@gmail.com 754-826-3039
Jeffry Bush jeffryb92@optonline.net 949-397-1831
Josh Benjamin jbenjamin65@gmail.com 609-482-9780
Mohamed Peck mpeck88@hotmail.com 480-944-6768
Keneth Rios rio8048@live.com 803-578-4079
Jeff Owen jarhuhq77@aol.com 740-757-4030
Lewis Curtis lcurtis51@live.com 866-589-2878
Waldo Christian waldoc76@me.com 276-754-5930
Rhett Compton rcompton27@yahoo.com 813-698-9067
Chas Frank cfrank48@gmail.com 419-776-9055
Gabriel Briggs gbriggs94@att.net 914-618-8277
Chang Kemp ckemp@outlook.com 484-757-3289
Joel Tillman jtillman@hotmail.com 833-559-8496
Thanh Pratt thanhp86@comcast.net 334-637-9844
Jerrod Blackwell jerrodb66@hotmail.com 703-991-2866
Brant Kidd bkidd3@mac.com 213-314-5841
Antonio Moody amoody@att.net 440-223-7802
Elmer Mathis emathis75@hotmail.com 954-793-2175
Efren Adkins eadkins81@live.com 561-397-1896
Jon Gibson jgibson42@hotmail.com 959-251-2438
Ivory Mercer imercer@outlook.com 717-802-4300
Moises Mooney mmooney77@icloud.com 717-785-7593
Stuart Barnes sbarnes99@verizon.net 832-216-4922
Herb Baxter xhkas57@icloud.com 303-973-9806
Xavier Hatfield xhatfield64@yahoo.com 614-606-2670
Odell Cantu cant705@me.com 268-276-2651
Basil Craig bcraig@outlook.com 700-574-4217
Raphael Mckay rmckay20@hotmail.com 409-477-5735
Edmundo Diaz edmundod56@msn.com 760-508-9852
Charles Abbott cabbott31@optonline.net 278-426-9095
Garret Mosley njulvhcn93@att.net 787-476-3853
Cyrus Maynard cmaynard16@gmail.com 787-691-9912
Armand Newman anewman77@verizon.net 351-885-2122
Julius Cantu jcantu@outlook.com 862-718-4191
Lacy Hancock lacyh31@sbcglobal.net 510-576-2942
Darnell Pate dpate81@optonline.net 856-249-2703
Wm Kemp wkemp90@msn.com 283-747-8595
Rod French zrspofejaq8@me.com 580-653-8630
Denis Mcintyre mcintyr4071@aol.com 570-718-5678
Lawrence
Alexander maljsrrm@me.com 260-546-5128
Gil Hamilton ghamilton@hotmail.com 500-453-3492
Norbert Randolph nrandolph86@aol.com 254-824-5463
Milton Nash mnash4@gmail.com 660-468-5254
Damon Potts dpotts97@optonline.net 320-495-8716
Mitch Wilkinson mwilkinson@aol.com 520-913-4849
Reynaldo Pickett rpickett25@att.net 615-931-7580
Alphonse Wolfe awolfe@comcast.net 214-884-3779
Faustino Crane fcrane93@live.com 507-334-3277
Hayden Carlson hcarlson78@hotmail.com 870-657-6522
Ethan Torres etorres40@hotmail.com 478-216-1711
Chester Sandoval sandova9646@live.com 514-896-7404
Sam Langley slangley@gmail.com 500-500-3314
Rafael Harrell vrwj74@icloud.com 763-924-7904
Ezequiel Hampton ehampton58@optonline.net 970-588-7047
Lewis Williamson imaucos@live.com 661-232-5367
Denis Valdez dvaldez60@me.com 562-518-8825
Lucien Glenn glen9@msn.com 628-344-5680
Morgan Lloyd mlloyd10@hotmail.com 969-653-3615
Courtney Reilly creilly61@sbcglobal.net 734-327-6388
Arturo Hobbs arturoh31@gmail.com 385-299-9749
Alberto Hoffman ahoffman@aol.com 712-661-3487
Arlie Hill hil3545@gmail.com 360-263-4384
Pete Ayala ayal9762@me.com 302-778-8742
Solomon Salazar 284-338-3975 aateg@aol.com
Clyde Evans 540-681-8060 cevans13@live.com
Burton Ware 219-692-2356 bware52@msn.com
Jermaine Chang 754-751-6646 jchang98@gmail.com
Carson Bryant 646-974-9671 carsonb3@verizon.net
Garland Meadows 511-708-3208 gmeadows25@optonline.net
Robert Craig 360-959-6205 rcraig20@me.com
Pete Bowen 517-382-3381 pbowen17@icloud.com
Cleo Roman 248-625-9398 croman18@optonline.net
Chet Gould 702-555-3916 oqjccy36@outlook.com
Pat Keller 316-324-9162 patk15@mac.com
Abdul Mcmahon 201-949-5545 amcmahon4@gmail.com
Brock Alston 712-527-1022 alsto3815@live.com
Ron Nguyen 416-878-7482 gazvrfrtk@mac.com
Antone Byers 787-868-6561 byer3769@outlook.com
Tad Rhodes 312-873-6991 trhodes86@hotmail.com
Pedro Christensen 706-427-9083 pchristensen42@icloud.com
Reginald Mitchell 877-666-4112 rmitchell60@comcast.net
Lon Sanchez 250-861-4906 lsanchez46@me.com
Quinn Stafford 586-397-4519 qstafford@yahoo.com
Armand Lancaster 620-579-2169 alancaster40@me.com
Oscar Morrison 508-405-5015 morriso963@live.com
Chad Hewitt 607-718-7246 hewit4282@att.net
Lou Espinoza 882-284-1717 lespinoza86@me.com
German Juarez 276-391-3652 juare3314@hotmail.com
Chase Bullock 920-671-2378 cbullock@icloud.com
Margarito Farley 975-201-8332 mfarley26@sbcglobal.net
Ramiro Wright 822-403-4750 wrigh2662@aol.com
Eddy Sherman 231-595-3324 esherman@hotmail.com
Clinton Doyle 631-975-3387 cdoyle@me.com
Monroe Stevens 305-907-3140 mstevens60@hotmail.com
Clay Tyler 412-638-7724 ctyler25@me.com
Ruben Graves 724-723-3759 wthg6@gmail.com
Lane Kirk 881-337-7390 lkirk72@optonline.net
Shayne Collier 757-809-2413 scollier53@comcast.net
Otha Brock 407-774-5107 othab30@comcast.net
Robby Jordan 915-287-5137 rjordan@verizon.net
Bret Garcia 910-869-3090 bgarcia71@aol.com
Marcellus Velasquez 606-276-4621 slzcwg65@gmail.com
Darell Kane 882-280-7095 dkane58@yahoo.com
Herb Joseph 509-429-1943 herbj15@gmail.com
Sergio Watts 541-475-7662 swatts20@yahoo.com
Jarrett Colon 309-508-1355 jcolon51@live.com
Graig Lester 740-267-4233 glester8@att.net
Tyler Alvarado 501-409-1473 talvarado94@msn.com
Harris Duran 801-504-1087 dura5281@aol.com
Nestor Page 559-670-5302 npage@aol.com
Perry Ellison 201-665-2121 pellison64@msn.com
Earl Cantrell 352-331-5192 ecantrell11@msn.com
Modesto Strong 802-352-7505 mstrong36@icloud.com
Galen Kidd 704-324-8184 gkidd39@optonline.net
Abe Melton 737-660-1617 abem94@mac.com
Salvatore Peterson 747-812-2712 lbzj22@live.com
Josh Franks 908-744-2720 jfranks@hotmail.com
Del Howe 330-492-1841 dhowe@mac.com
Vicente Wolf 940-822-6951 vwolf38@live.com
Jordan Bass 818-252-2721 jordanb7@aol.com
Santos Sanders 913-432-1517 zcochs@yahoo.com
Jarred Farmer 662-620-8019 jarredf49@me.com
Ezekiel Allison 904-409-8657 ezekiela44@gmail.com
Eloy Love 956-460-2704 elove16@att.net
Kevin Delaney 412-984-5650 zjyjmxqmra62@outlook.com
Chase Valenzuela 405-295-7426 cvalenzuela48@att.net
Ken Schroeder 662-232-8483 ukxetboxf@outlook.com
Dillon Thornton 911-729-7310 dthornton13@live.com
Kristopher House 704-597-7710 hous49@mac.com
Lucio Douglas 646-401-4421 ldouglas76@outlook.com
Alfonso Butler 947-418-2138 abutler32@live.com
Dwain Murphy 512-617-6333 dmurphy62@sbcglobal.net
Chung Simon 617-608-5697 csimon@att.net
Nathanael Randolph 918-836-5453 kwtvektf11@gmail.com
Russ Padilla 660-723-4047 russp63@gmail.com
Charles Williams 340-243-5059 cwilliams97@verizon.net
Evan Watkins 567-645-6231 ewatkins92@aol.com
Travis Munoz 312-321-3459 iemcbryipl69@sbcglobal.net
Kasey Mendez 664-390-4772 kmendez27@comcast.net
Abdul Owen 704-806-7715 aowen44@sbcglobal.net
Laurence Levine 811-529-6184 llevine9@mac.com
Mauro Blackburn 440-883-4270 mblackburn7@hotmail.com
Waldo Faulkner 704-851-1305 uxuhoxw88@hotmail.com
Lewis Pruitt 306-308-5554 lpruitt@gmail.com
Kent Carson 669-287-1101 ixzpuyo66@hotmail.com
Earle Rogers 606-301-9233 erogers2@comcast.net
Lacy Cortez 603-619-3984 lcortez@gmail.com
Moshe Eaton 369-388-5135 meaton70@mac.com
Gale Hodge 211-804-9027 ghodge@sbcglobal.net
Columbus Ellison 609-603-5875 columbuse82@outlook.com
Buddy Davenport 807-633-8743 bdavenport@mac.com
Jonah Winters 574-288-7526 winter5659@att.net
Reuben Estes 442-493-2585 restes3@verizon.net
Alexander Mcintosh 867-973-4264 alexanderm24@msn.com
Hilton Mann 614-534-6204 hmann59@yahoo.com
Chester Valenzuela 705-967-9230 cvalenzuela67@me.com
Rory Frazier 229-749-9282 rfrazier61@optonline.net
Sid Campos 850-461-5256 scampos93@yahoo.com
Ken Dawson 868-388-6332 gefcnxvuo28@gmail.com
Roland Buck 809-571-4553 rbuck46@verizon.net
Jeffery Bray 704-894-9878 jbray68@optonline.net
Alfred Britt 714-915-5120 abritt10@msn.com
Mike Howell 671-514-2487 mhowell@sbcglobal.net
Cedric Harrell 848-959-8580 charrell@gmail.com
Antione Baker 712-778-8373 abaker@icloud.com
Graig Morrison 800-419-7915 graigm83@aol.com
Alex Cantu 767-760-9879 acantu31@verizon.net
Cristobal Green 920-514-8429 cgreen81@icloud.com
Toby Pearson 979-615-8194 pearso1658@gmail.com
Kirk Cote 407-368-1707 zgnpqlhltg94@icloud.com
Albert Chaney 517-934-5775 achaney35@me.com
Lino Harper 484-864-4308 lharper37@aol.com
Gerald Jacobs 882-932-5737 jacob3024@icloud.com
Lindsay Malone 216-535-7866 lmalone15@icloud.com
Joseph Goff 586-712-7233 jgoff10@icloud.com
Glen Head 678-692-2952 hea9668@msn.com
Tyree Vazquez 605-987-7999 tvazquez69@att.net
Teddy Golden 714-572-3513 tgolden74@comcast.net
Vern Mason 650-877-3804 vmason@sbcglobal.net
Miguel Leach 341-579-1479 leac289@yahoo.com
Lauren Mason 210-760-8311 laurenm75@aol.com
Tommie Vinson 204-838-7059 jgwjfme29@yahoo.com
Allen Hopkins 424-452-8638 ahopkins61@att.net
Warner Mcgowan 731-702-4288 warnerm72@hotmail.com
Kip Floyd 706-840-4421 kfloyd76@hotmail.com
Kirk Slater 239-202-9045 slate638@gmail.com
Tracey Moon 456-417-9695 tmoon80@outlook.com
Ronald Knowles 331-901-2186 rknowles64@verizon.net
Elton Chapman 832-700-5909 echapman@sbcglobal.net
Jasper Saunders 615-855-2852 jsaunders@icloud.com
Craig Cabrera 518-958-2402 cabrer5597@sbcglobal.net
Roger Ruiz 262-997-7396 rruiz80@msn.com
Sid George 564-927-4219 sidg22@me.com
Deangelo Vaughan 511-532-2766 deangelov98@msn.com
Sidney Reeves 913-302-1126 sreeves53@live.com
Porfirio Moon 623-819-8400 pmoon84@att.net
Jonah Serrano 312-974-7442 jserrano@comcast.net
Alvaro Fuentes 830-703-5401 alvarof71@att.net
Darwin Walters 767-708-9905 walter6016@me.com
Riley Gallagher 416-760-6930 rgallagher46@live.com
Josh Coleman 740-835-9107 jcoleman@yahoo.com
Jarvis Skinner 919-309-9882 jarviss1@hotmail.com
Elroy Carroll 806-955-2940 zvslhawecs@live.com
Robt Randolph 517-690-7444 rrandolph68@gmail.com
Rocco Rodriguez 754-521-8827 rrodriguez17@optonline.net
Avery Morales 757-950-9394 amorales91@outlook.com
Travis Avila 801-582-1623 tavila@att.net
Rico Byrd 602-334-2268 pjro@gmail.com
Alfonso Rogers 720-231-4309 arogers@me.com
Zackary Mueller 413-219-2761 zmueller88@optonline.net
Randall Davis 832-308-7198 rdavis3@gmail.com
Pasquale Chen 763-392-6690 pchen@outlook.com
Hai Contreras 208-717-9659 haic98@verizon.net
Dewey Donovan 410-794-4397 ddonovan50@att.net
Wendell Bowman 900-510-8520 wendellb26@icloud.com
Miles Carpenter 811-923-5052 mcarpenter51@msn.com
Marlin Thornton 604-456-6749 mthornton27@yahoo.com
Peter Love 708-959-5284 ahanaqwcvp28@yahoo.com
Evan Pittman 717-451-2756 isd@aol.com
Carroll Bullock 337-672-7915 cbullock49@me.com
Rosendo Kirby 859-834-4141 rosendok42@yahoo.com
Jarrod Wilson 310-296-4069 jwilson@hotmail.com
Tyler Richard 409-712-6453 trichard@me.com
Sammie Pace 501-840-6906 space@sbcglobal.net
Marcellus Acevedo 754-653-6084 macevedo10@gmail.com
Mario Atkins 264-590-6665 marioa41@hotmail.com
Donnie Finch 564-637-2215 dfinch84@sbcglobal.net
Lucius Mcdaniel 713-290-9465 lmcdaniel33@hotmail.com
Alvin Hutchinson 900-446-5048 aleh24@yahoo.com
Benny Ward 719-895-9108 bward25@att.net
Paul Wallace 682-385-9427 pwallace@optonline.net
Courtney Beck 420-722-2968 cbeck64@att.net
Junior Maddox 660-344-4688 jmaddox85@sbcglobal.net
Rey Acosta 208-419-8576 racosta@live.com
Carlo Cruz 810-517-6381 ccruz33@optonline.net
Chadwick Juarez 464-625-4489 chadwickj@aol.com
Dean Hooper 775-410-7394 hoope23@me.com
Ramon Lara 327-640-3130 lar52@comcast.net
Jewell Petty 710-817-5065 jpetty@me.com
Max Warren 802-677-2487 mwarren@outlook.com
Elvis Miranda 464-590-4144 elvism@comcast.net
Jewell Clarke 317-204-9567 nuu61@icloud.com
George Christensen 752-688-3779 christense3094@icloud.com
Gavin Poole 360-506-5027 gpoole13@att.net
Seth Paul 414-485-6912 spaul62@optonline.net
Sammie Ellison 737-369-5205 sellison37@comcast.net
Barton Nichols 224-932-7915 nichol6482@sbcglobal.net
Brett Patterson 660-317-1885 bpatterson6@yahoo.com
Isidro Nieves 304-331-3182 inieves71@comcast.net
Kent Faulkner 661-892-8158 kfaulkner7@mac.com
Charles Bolton 709-560-6738 cbolton@live.com
Josiah Knight 623-754-9047 iyccvuo93@aol.com
Lupe Benjamin 613-644-1136 benjami8413@optonline.net
Elliot Gonzalez 206-501-5134 elliotg37@me.com
Bobby Dean 641-659-3811 bdean72@aol.com
Amos Price 717-690-6787 aprice95@hotmail.com
Kerry Schroeder 260-446-7362 kschroeder@comcast.net
Wes Pate 417-354-6961 wpate99@verizon.net
Cleveland Mann 415-375-3287 cmann79@live.com
Norbert Vinson 385-868-1852 nvinson8@hotmail.com
Milton Wade 931-883-8104 mwade90@gmail.com
Lauren Barnett 573-991-4106 lbarnett80@sbcglobal.net
Cary Kirby 859-271-7097 ckirby9@msn.com
Biostatistician Clark Salinas 845-641-5553 csalinas16@mac.com
Officer Hugo Cross 500-760-4858 hcross@optonline.net
Assistant Domenic Molina 256-975-9610 dmolina@me.com
Intelligence Calvin Ayers 337-838-9148 calvina46@optonline.net
Counting Thomas Sawyer 352-421-3126 tsawyer14@live.com
Representative Danny William 600-925-9300 dwilliam23@comcast.net
Sales Samuel Solomon 505-206-9958 ssolomon59@icloud.com
C-Level Sydney Sutton 835-752-9580 ssutton97@outlook.com
Well Stewart Harrell 701-478-9209 harrel9997@icloud.com
Manager Ken Gardner 248-330-7997 kgardner63@msn.com
Receptionist Eddie Emerson 308-996-8347 eemerson@att.net
Sales Roosevelt Welch 700-827-1719 rwelch10@verizon.net
Business Ernie Russell 620-789-4914 erussell@sbcglobal.net
Director Josef Holder 767-759-3917 jholder76@comcast.net
Metal Fletcher Johns 664-249-7260 fletcherj30@icloud.com
VP Bryce Ortega 734-953-8555 bortega64@aol.com
Administrator Sheldon Lester 670-461-8880 leste5473@sbcglobal.net
Media Lenard Berry 661-543-3087 lberry46@sbcglobal.net
Technology Merrill Chan 719-476-8186 mchan@yahoo.com
Chief Chi Cameron 336-785-6554 ccameron69@att.net
Improvement Young Joyce 270-966-2464 hmpvqjoa46@outlook.com
Social Quincy Schroeder 609-767-9156 schroede2388@sbcglobal.net
Engineer Refugio Lopez 671-478-1186 rlopez58@gmail.com
Operations Nelson Fox 636-205-1065 nfox93@gmail.com
Brand Chang Glass 708-519-6690 cglass17@verizon.net
Producer Arnoldo Maynard 567-993-7583 maynar1865@hotmail.com
Orderly Donnell Dudley 323-311-8849 dmfovekv30@me.com
(CIO) Britt Stout 954-290-5167 stou1718@gmail.com
Chief Gilbert Dillon 737-908-8008 gdillon46@live.com
Sales Rodrick Rojas 724-458-5072 rrojas79@sbcglobal.net
Authorizer Dewitt Vega 281-349-5499 dvega19@att.net
Painter Greg Bradford 262-820-4152 gbradford77@verizon.net
Sales Ismael Hood 606-234-6374 ihood41@comcast.net
Media Javier Robinson 709-585-7066 javierr@msn.com
Engineer Zack Marquez 450-634-7241 zmarquez48@live.com
Payable/Receivable Brice Compton 580-596-6155 bcompton58@mac.com
Entry Damien Weaver 464-308-4946 dweaver90@aol.com
Geological Scott Gibbs 918-309-9419 sgibbs76@mac.com
Officer Benjamin Ferrell 213-748-2704 ziaqn32@live.com
Coordinator Delbert Morrison 563-448-3826 dmorrison48@verizon.net
Representative Isaiah Freeman 331-792-6315 ifreeman@outlook.com
of Hector Hess 732-387-3313 hhess38@aol.com
Entry Dana Massey 246-581-8092 dmassey@verizon.net
Biological
Kristopher
Petersen 562-851-4009 qdkmws84@mac.com
Public Boris Rivers 240-895-6681 brivers@yahoo.com
Medical Jorge Harrison 858-334-8209 jharrison90@comcast.net
Officer Maurice Casey 334-830-4816 mcasey42@outlook.com
Cloud Enrique Sawyer 234-996-5407 esawyer71@mac.com
Graphic Jewell Downs 415-598-3660 jdowns47@me.com
Officer Ellis Weber 835-677-9574 eweber36@me.com
Computer Lee Best 276-748-3451 leeb42@msn.com
Benefits Alden Whitney 330-499-3030 whitne8050@att.net
Office Andre Pickett 585-858-1317 picket3817@live.com
Loan Alonso Woodard 551-513-1029 awoodard86@mac.com
Laboratory Stan Cleveland 937-818-1903 scleveland23@aol.com
Customer Vance Prince 618-678-4534 vprince47@outlook.com
Associate Kirby Hensley 612-533-9615 khensley@comcast.net
Associate
Rolando
Chapman 803-434-1882 rchapman23@comcast.net
Outside Eric Ball 406-895-8654 ericb55@gmail.com
Pipefitter Hilton Matthews 516-281-3409 hmatthews@outlook.com
Assistant Daryl Duke 830-449-7659 pzqzby10@sbcglobal.net
Manager Logan Jacobson 339-410-7481 ljacobson@comcast.net
Sales Jeremiah Rivas 234-821-7223 vvqvizja8@me.com
C-Level Eliseo Bauer 954-550-9499 tdjk78@msn.com
Representative Hugo Justice 253-542-2779 justic7939@optonline.net
Pharmacist Wilfred Lloyd 764-390-6339 wlloyd@aol.com
Engineer Homer Pierce 985-687-2410 pierc3069@icloud.com
Account Lawerence Sweet 800-590-9014 lawerences@live.com
Technician Bobby Grimes 682-780-2792 bgrimes@att.net
Supervisors Shon Pittman 600-756-2467 pittma7860@icloud.com
Supervisor Lloyd Holloway 401-866-3137 lholloway71@verizon.net
(CIO) Edwin Pratt 307-263-3138 epratt@aol.com
Analyst Lionel Bush 937-900-4399 lbush@msn.com
Developer Williams Sawyer 864-281-9229 sawye65@yahoo.com
Ethical Abram Haney 671-786-3117 cbtuky10@aol.com
Coordinator Barney Sanchez 516-809-9156 bsanchez28@outlook.com
Cleaner Robert Jefferson 502-231-2744 rjefferson68@optonline.net
Engineer Rosario Moses 352-944-3271 rmoses@me.com
Researcher Jesse Guthrie 877-969-3462 jguthrie76@outlook.com
Consultant, Franklin Mitchell, 402-787-1071, franklinm19@msn.com
Financial, Odell Blackburn, 809-961-6647, blackbur9571@gmail.com
Taper, Chad Cervantes, 415-950-8689, ccervantes77@msn.com
Care, Chet Durham, 224-525-5964, cdurham50@msn.com
Relations, Leslie Lester, 901-981-1453, toixcrjopk79@hotmail.com
Manager, Conrad Acosta, 309-738-4792, svrxmkxp@comcast.net
CIO—Chief, Pat Dickson, 868-453-1548, pdickson14@msn.com
Administrator, Tony Alford, 425-667-1206, talford73@live.com
Computer, Maximo Molina, 847-242-1903, maximom58@me.com
Motion, Dale Silva, 360-923-6219, silv58@outlook.com
Associate, Tim Ferrell, 236-831-4749, tferrell82@verizon.net
Digital, Lavern Briggs, 646-573-7286, lbriggs59@hotmail.com
Brand, Clyde Sellers, 880-758-9012, rcn14@optonline.net
Resources, Rolland Miranda, 814-825-6659, rmiranda90@verizon.net
Manager, Ned Davenport, 868-537-8850, ndavenport8@gmail.com
Medical, Alden Kirby, 574-528-9602, akirby82@comcast.net
Computer, Antione Harvey, 732-995-8604, aharvey7@aol.com
Operating, Bret Bruce, 513-704-8737, bbruce99@me.com
Lead, Nathanael Marsh, 202-689-6810, nmarsh@aol.com
Artificial, Odis Nunez, 201-626-6879, onunez@sbcglobal.net
Film, Manual Brennan, 510-505-3719, mbrennan@live.com
Solar, Bart Donovan, 717-297-6940, bdonovan41@outlook.com
Electrical, Delbert Burt, 405-437-7498, dburt20@optonline.net
or, Rocco Stone, 860-529-5931, rstone1@att.net
Assistant, Rico Blackwell, 445-306-1341, rblackwell@mac.com
SQL, Seymour Gordon, 236-269-1791, sgordon2@aol.com
Payroll, Gail Lang, 828-668-6177, glang5@live.com
Robot, Noe Myers, 289-953-2219, aupqzrku84@outlook.com
Novelist/Writer, Ryan Estrada, 767-781-1015, llsfmma@icloud.com
Solar, Cristobal Wiggins, 905-210-9724, cwiggins60@optonline.net
Production, Solomon Bolton, 218-846-8390, bolto28@mac.com
Product, Darius Riley, 918-517-2683, pleduuntz68@icloud.com
Retail, Parker Cameron, 865-218-2016, pcameron64@mac.com
Officer, Gus Pollard, 283-951-6724, gpollard8@hotmail.com
Hacking, Deshawn Reyes, 737-733-5204, dreyes50@icloud.com
Personal, Jude Gallegos, 240-679-3122, judeg74@optonline.net
Product, Emmett English, 509-813-6551, eenglish29@mac.com
Impressions, Fred Mcintyre, 916-367-3767, fmcintyre8@mac.com
Drafter, Rex Tillman, 920-535-4810, rtillman@icloud.com
Manager, Milton Joyner, 602-767-1562, mjoyner73@mac.com'''

phoneNumberPattern = re.compile(r'''
# formats supported
# (479) 205-4874
# 479-205-4874
# 205-4874
# 205-4874 ext 3326
# 205-4874 ext. 3326
# 205-4874x3326
((\(?\d\d\d\)?( |-))?               # area code
\d\d\d-\d\d\d\d                     # phone number
(( ext(.)? \d[2-5])|(x\d{2,5}))?)   # extension
''', re.VERBOSE)
phoneNumberResults = [number[0] for number in phoneNumberPattern.findall(text)]
emailPattern = re.compile(r'''
([a-zA-z0-9_.-]+
@
[a-zA-z0-9-]+
.
[a-zA-z0-9-]{2,})
''', re.VERBOSE)
emailResults = [email for email in emailPattern.findall(text)]
prettyResults = '\n'.join(phoneNumberResults + emailResults)
print(prettyResults)
