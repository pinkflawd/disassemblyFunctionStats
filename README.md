# disassemblyFunctionStats
Comparing function detection of R2 and IDA

Call both scripts to fill the database:

python funcCountR2.py [dir]

python idaPython.py [dir]

Note:
[dir] needs to be a directory containing Windows PE files, best named after file hashes. 
funcCountIDA.py currently contains a dummy path, needs to be fixed before running.
For flushing the DB, funcCountR2.py contains two lines of code that can be uncommented. 

The project is a proof of concept and serves debugging purposes only, don't expect wonders ;)


Numbers from malware function detection, sorted by total difference descending:

| SHA1                                     | R2 count | IDA count | Diff | Percent |
|------------------------------------------|----------|-----------|------|---------|
| a884b73fa3c0861071bc8c4cd94228e985615e48 | 1767     | 960       | 807  | 0.46    |
| 9087ecc840d67b0cb718f1b94206d5f2b50e8c33 | 561      | 278       | 283  | 0.5     |
| f646a0e40ae391521a5cf5afe8cb5cf5047d9964 | 1785     | 1616      | 169  | 0.09    |
| 441d7b8362480e872ae9e0ee784fbd7dd41f18c9 | 325      | 195       | 130  | 0.4     |
| 8a1ca6a0f97ae6a8777d3a080f9080174a867da1 | 482      | 395       | 87   | 0.18    |
| 8feb3ff918da441b2b147b62325a98d06e40eef4 | 107      | 22        | 85   | 0.79    |
| c6b65da68f93e2ab2d55d6073ce498d95fdbe8bf | 403      | 325       | 78   | 0.19    |
| c4d86c3fed2277c8ab00dc4cad35204437a1b89f | 457      | 383       | 74   | 0.16    |
| 2d8550af89ad7a964566e090036c0cd75e7cdddc | 288      | 217       | 71   | 0.25    |
| 78b625381d2ef60d064ceab23b849a86b981fb12 | 153      | 91        | 62   | 0.41    |
| 62bc57417a42d7199c909c8c81616d5767a0851d | 341      | 291       | 50   | 0.15    |
| 64dc26f176e16a7ad0111eecc48f401fac4cccfc | 49       | 2         | 47   | 0.96    |
| 830ab386db5e0f5cf89598b683f4eaaf4380baaa | 101      | 55        | 46   | 0.46    |
| 2e731d396571254744dc3643c9c4970d49428c38 | 105      | 63        | 42   | 0.4     |
| e644e7c08dbd5e0d71c7ebd2857df8d59d9f170a | 104      | 63        | 41   | 0.39    |
| 58d9b1c60a297d71ccd0c433e85e2cec80f0580a | 63       | 27        | 36   | 0.57    |
| a40af8a05c9d4101b38b48f274e52d264f58ea38 | 42       | 10        | 32   | 0.76    |
| dbb06368141a4af8704437202fb85f709b13473c | 163      | 139       | 24   | 0.15    |
| defe2b01b05afcc356d6911fdaa1ca0cf1f6951a | 160      | 139       | 21   | 0.13    |
| 4f843e2c8270f594fa016af6bf12de36cfb83232 | 62       | 43        | 19   | 0.31    |
| a7bd9df39af9da135d81180ba802e8ec1407624c | 101      | 82        | 19   | 0.19    |
| e841ca216ce4ee9e967ffff9b059d31ccbf126bd | 27       | 10        | 17   | 0.63    |
| 161f950df5a75b557f2c200d5dc2498937990475 | 31       | 16        | 15   | 0.48    |
| 315fbb2fb4dcb103839d7a307a7c39a47b9bfe27 | 134      | 120       | 14   | 0.1     |
| 5a9a634a2b6b8516b43da27a8a6003d161d33424 | 134      | 120       | 14   | 0.1     |
| d6d7b69292f471453a50a7d07fc590edada36367 | 38       | 25        | 13   | 0.34    |
| 2453dab3b42af9f25e38e22fcd39ff68f35755c3 | 45       | 33        | 12   | 0.27    |
| bd278188e922e1ee70b4f5761a68c37f03634126 | 108      | 97        | 11   | 0.1     |
| 32b1b98177cfc94d515b76e24b09003e9a241c2b | 36       | 26        | 10   | 0.28    |
| 430f578d2ec7e4d781067340ebf90a9ee3f1f4da | 507      | 497       | 10   | 0.02    |
| 6efb12d11d2719bd8f5ca2a44ad418f703f4791b | 123      | 113       | 10   | 0.08    |
| 9093426aaf166ae7b7a4d658418f6e316142cdbd | 11       | 1         | 10   | 0.91    |
| a693f6202a0b09841678fb0d6932ba1bd736ab4a | 21       | 11        | 10   | 0.48    |
| dbca702ec71bc775cc164acc053d5f09ce0803f3 | 130      | 121       | 9    | 0.07    |
| f75d59e152e0cbfc70b08f9c443c0c44f2e3474a | 27       | 18        | 9    | 0.33    |
| a9c567a845d2f7ef2d7977f5f0e507c73e7a0437 | 130      | 122       | 8    | 0.06    |
| b2f7b6a60a1a577ae87740058f7a9857d1101eb6 | 18       | 10        | 8    | 0.44    |
| 189c1f5a8a2efaf6477bc3208bb72971eca081d3 | 20       | 13        | 7    | 0.35    |
| 4d0df7ec508da6837588cafd84f19ad53dac102a | 189      | 182       | 7    | 0.04    |
| 151e04886df09fc5c85a0b92ab22cad8264ae9a1 | 143      | 137       | 6    | 0.04    |
| 63b65772bdabb67667d41dca8164117bd7c056e5 | 118      | 112       | 6    | 0.05    |
| f5cca03810490d924a234be61c680b190a96571e | 299      | 293       | 6    | 0.02    |
| 9adb98e85d69d6fad77249e4a34fb87a8182fbd8 | 11       | 6         | 5    | 0.45    |
| f2827e49cfbc6f251afb075abc236825678a0611 | 8        | 4         | 4    | 0.5     |
| 5d538159186729d42885be4be8253a1d25c41dde | 194      | 191       | 3    | 0.02    |
| 0e8ca304d7907f2d01a3cad2ac8334cde4e53dd8 | 10       | 8         | 2    | 0.2     |
| 124d70832f595af5b45bfc798623567d699e05bf | 183      | 182       | 1    | 0.01    |
| 25a08e26773ebd5bcbf7d51586d5dc863acc0204 | 2        | 1         | 1    | 0.5     |
| 5966f710ccf432427c5c333bae63431dd22127c5 | 2        | 1         | 1    | 0.5     |
| 77102ad5d99913d5d4187060566d34cef45f468b | 44       | 43        | 1    | 0.02    |
| 784239d65a00516e3bc9c88714f17d0ffa39c263 | 2        | 1         | 1    | 0.5     |
| 85a71025a325a5ac840e6a929b527cd8911926fe | 364      | 363       | 1    | 0.0     |
| a2c1719127d6e239fe9958f959f93893ff95593b | 183      | 182       | 1    | 0.01    |
| 49352a95766a39aa537a9c4dc8119cc02f9975d3 | 34       | 38        | -4   | -0.12   |

Numbers from Win8 64-bit binaries:

| SHA1                                     | R2 count | IDA count | Diff | Percent |
|------------------------------------------|----------|-----------|------|---------|
| b642e9fcfac93f219d07bb6d530eb1de9efeb511 | 9386     | 5911      | 3475 | 0.37    |
| 7ffebfee4b3c05a0a8731e859bf20ebb0b98b5fa | 2558     | 1355      | 1203 | 0.47    |
| 1aa232b8c544d78c73f8a6baebbdbac7b533d98e | 2944     | 1802      | 1142 | 0.39    |
| 04a66cc5575613c178e6d5d2adb1f5340f41b5fd | 526      | 282       | 244  | 0.46    |
| 5bfda39e94a5d7862aecd87856d1475d0fe6e96d | 1354     | 1194      | 160  | 0.12    |
| dacd720d116d7261d4a015287e02b8fe03592c3a | 788      | 659       | 129  | 0.16    |
| a3b46609d159615d5c78f5c54ea24d46805ce374 | 232      | 124       | 108  | 0.47    |
| b6368bda63d42bd0050ea071888528cb9d0cb5a8 | 132      | 71        | 61   | 0.46    |
| d92befb08729b644d67ef4ba6c8b3874959cc890 | 439      | 391       | 48   | 0.11    |
| 56e64264999fcda57852e2fb0e5bc3cc45ef4ccf | 290      | 253       | 37   | 0.13    |
| 4d4957b7eb8dfad23da7d584bdc5799aaa5a4641 | 207      | 196       | 11   | 0.05    |
| 62feb04d2d7f0201fb8b504f800d8aee941ef583 | 37       | 31        | 6    | 0.16    |
| 5b0732adae033cac60b0c8f6f0602072e3770a99 | 253      | 250       | 3    | 0.01    |
| 27cdeb38a55826936d5b55f54984447398c5d996 | 25       | 24        | 1    | 0.04    |
| 7bd11624f84c992481dae9f96ea6744bb7ad40c9 | 335      | 335       | 0    | 0.0     |
| acf68c210ca36f6961ac6f8b92c6ef95ff1cbdf4 | 30       | 30        | 0    | 0.0     |
| fa45d062349f34ef477f4aed35b0c51d221cf784 | 98       | 99        | -1   | -0.01   |
| 6d6d9b78c9a3999ff2f803107c0a57d6ccdfdcb6 | 821      | 1038      | -217 | -0.26   |
| 0862bae3dc3a0b5c609867d1a7086f1954f2f556 | 1325     | 1751      | -426 | -0.32   |

Numbers from Win8 32-bit binaries:

| SHA1                                     | R2 count | IDA count | Diff | Percent |
|------------------------------------------|----------|-----------|------|---------|
| 051bfe73d395973f5679dba2309f70906de67829 | 3065     | 1740      | 1325 | 0.43    |
| a44af16487babd1f625964ec53ce6bd5d9672a22 | 2594     | 1373      | 1221 | 0.47    |
| c0ae1f729dc0d7fa5132200a4f54cb26a2af70e1 | 1964     | 1256      | 708  | 0.36    |
| 98a9ac93fe31f38f47f38db78bf12fa0c6214f9a | 944      | 467       | 477  | 0.51    |
| 9cff7f11e977200a9326c22d17463262de8f0a2b | 486      | 245       | 241  | 0.5     |
| 36e870c189f1a5006ac7d989cdfc160ec07f3b5a | 1011     | 805       | 206  | 0.2     |
| b1b9e83f5adf8bf22ce9f4943775a9d8f52a87e5 | 593      | 434       | 159  | 0.27    |
| c632ae4d41821da3f16d8678fb29a880c2035a4a | 305      | 158       | 147  | 0.48    |
| 927592cfea4497a27fe95af9978ffb9e93cb85af | 343      | 317       | 26   | 0.08    |
| 911d81d9c7df4d63c33f51f758ba26489808c4e2 | 813      | 788       | 25   | 0.03    |
| 36a13e7f9bb93218695b391b387407b9c197c1ba | 394      | 380       | 14   | 0.04    |
| e6429de6fc6d117e203455be9a8d6f475428b658 | 232      | 222       | 10   | 0.04    |
| 14acdb96c0cf537b20099962b2536bca48775dc4 | 48       | 42        | 6    | 0.13    |
| 64428d1a4aad359c78155d1bcf96bad98162dbb0 | 42       | 36        | 6    | 0.14    |
| 9c3e75f34fec80660a754aff4d213810a2753d66 | 34       | 28        | 6    | 0.18    |
| a29930dd7dc2ba835bdf648ba20a273939c7815d | 51       | 45        | 6    | 0.12    |
| 18befbfc692df3d6b2205a90a70e64e1787bd11b | 35       | 32        | 3    | 0.09    |
| 4d0c5033fadf53bdd0ff330f0ec146df5f7104cf | 169      | 233       | -64  | -0.38   |
