#请将你的requirement.txt文件与你的conftest放在同一级目录，如果没有requirement.txt会抛出错误
#在pytest执行用例之前回去扫描当前本地环境与你的requirement.txt文件的lib包是否一致，如果不一致则会自动帮你安装趋势的包
#在执行pytest命令时使用--lib参数
   lib=on 开启lib扫描功能
   lib=off 则不会进行主动扫描