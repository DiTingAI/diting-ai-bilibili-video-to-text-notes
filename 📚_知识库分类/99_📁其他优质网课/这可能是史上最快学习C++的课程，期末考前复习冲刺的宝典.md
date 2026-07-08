# 📝 这可能是史上最快学习C++的课程，期末考前复习冲刺的宝典

> ### 🎯 谛听 AI (diting.cc) 网页端免登录生产力直达
> 本篇语义笔记由 **`https://diting.cc`** 官方高并发多线程引擎全自动生成。
>
> 🛑 **因 GitHub 网页端排版局限，本篇笔记对应的：**
> * 📊 **100% 还原的全局嵌套【可视化思维导图】**
> * 📈 **基于视频核心逻辑提炼的【核心待办行动清单】**
> * 🚀 **一键直接洗稿成小红书、抖音脚本、知乎回答的【多矩阵创作者洗稿工具】**
>
> **均已在 diting.cc 云端后台同步生成完毕！**
> 👉 **`https://diting.cc`**，微信扫码 1 秒免密登录，即可直接查看、免积分导出该课程的**高清思维导图与全套洗稿文案**！

---
## 📝 逐字稿（带可点击时间戳）

> 点击任意 `[00:15:23]` 时间戳，直达 B 站原视频对应秒数


[00:00:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=0) - 大家好，今天我们用100分钟左右的时间来学习C++。
[00:00:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=5) - 什么是C++呢？
[00:00:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=6) - C++是一种跨平台的语言。
[00:00:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=8) - 可以用于创建高性能的应用程序。
[00:00:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=11) - C++是由Bjarne这哥们儿开发的。
[00:00:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=14) - 作为C语言的一个扩展。
[00:00:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=16) - C++同时为程序员也提供了对系统资源和内存的高度控制。
[00:00:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=19) - 该语言在11年、14年、17年进行了三次大的变更。
[00:00:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=22) - 即C++11、C++14和C++17。
[00:00:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=30) - 为什么使用C++呢？
[00:00:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=32) - 因为C++是世界上最流行的语言之一。
[00:00:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=35) - 在今天的操作系统，包括图形界面，还有一些嵌入式系统中，都可以看得见C++的身影。
[00:00:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=44) - C++作为一种面向对象的编程语言，它为程序员提供了清晰的结构，也便于复用，所以降低了开发成本。
[00:00:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=53) - 同时C++也具有可移植性，开发以后可以使用于各个多平台的应用程序。
[00:01:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=61) - C++也比较有趣，也比较好学。
[00:01:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=64) - 由于C++和C语言比较接近，所以程序员也很容易从C++转到C语言，反之也是一样的。
[00:01:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=77) - 好，我们今天学习的主要内容有第一语法，输出、注释、变量，输入、数据类型，运算、字符串，条件语句、switch，循环语句，数组、指针，函数、类，多态性、文件和异常处理。
[00:01:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=99) - 首先我们来看C++开发环境的安装。
[00:01:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=105) - 我们首先打开MingGW的官网。
[00:01:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=108) - MingGW-W64.org。
[00:01:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=111) - 然后我们去点Download。
[00:01:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=114) - 我们可以看到，它这里是支持Windows的。
[00:01:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=119) - 这里有个Source，Source里面，它这里有个Source Folder。
[00:02:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=123) - 我们点击这个Source Folder。
[00:02:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=126) - 我们看到这里直接有下载，但我们先不要下它，我们往下拉。
[00:02:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=130) - 这里有一个MingGW的Online的安装包。
[00:02:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=136) - 我们点击下载它。
[00:02:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=138) - 我们可以看到这里下载完成。
[00:02:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=140) - 我们点击打开。
[00:02:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=142) - 然后这里版本我们可以不用管它。
[00:02:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=147) - 这里架构，我们是X86 64位的，线程是W32的，异常处理我们可以选SEH。
[00:02:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=158) - 这个目录我们也可以不用管，就让它安装到这里，当然你也可以自己改目录。
[00:02:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=164) - 这样就开始安装了。
[00:02:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=169) - 我们点下一步。
[00:02:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=176) - 这样就安装完成了。
[00:02:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=179) - 然后我们打开这个安装目录。
[00:03:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=181) - 我们找到这个bin目录。
[00:03:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=183) - 我们把这个地址复制下来。
[00:03:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=189) - 然后我们打开计算机属性。
[00:03:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=191) - 环境变量里面，系统变量里面的Path。
[00:03:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=197) - 然后我们在这里添加进来。
[00:03:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=201) - 确定。
[00:03:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=205) - 再确定。
[00:03:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=207) - 我们打开个命令窗口。
[00:03:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=212) - 我们运行GCC。
[00:03:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=226) - 然后这里直接就有下载Windows的。
[00:03:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=228) - 我们点击。
[00:03:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=230) - 下载成功我们直接点击安装。
[00:03:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=232) - 然后它会弹出这么一个警告。
[00:03:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=235) - 我们可以直接点确定。
[00:03:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=237) - 然后点我同意协议。
[00:03:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=239) - 下一步。
[00:04:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=241) - 这里可以选下安装目录。
[00:04:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=243) - 它默认安装在这里。
[00:04:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=246) - 再点下一步。
[00:04:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=248) - 然后再点下一步。
[00:04:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=252) - 开始安装。
[00:04:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=255) - 安装完成。
[00:04:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=258) - 我们打开Visual Studio Code。
[00:04:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=260) - 这个按钮。
[00:04:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=262) - 这个就是一层Sense。
[00:04:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=264) - 然后我们在这里输入C++。
[00:04:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=266) - 它就会查出来。
[00:04:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=268) - 第一个就是这个图标。
[00:04:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=270) - 然后我们点击安装。
[00:04:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=272) - 这样就可以安装成功了。
[00:04:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=276) - 好，我们来看C++的语法。
[00:04:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=280) - 这是一个标准的C++程序。
[00:04:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=287) - 我们看第一行。
[00:04:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=289) - 警号Include。
[00:04:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=291) - 尖括号IOStream。
[00:04:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=293) - 尖括号。
[00:04:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=295) - IOStream是一个头文件库。
[00:04:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=297) - 它让我们与输入输出的对象一起工作。
[00:04:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=299) - 它让我们与输入输出的对象一起工作。
[00:05:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=301) - 例如第00:05:03 - 五行的 Cout。
[00:05:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=305) - 例如第五行的 Cout，就可以使用这个。
[00:05:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=307) - 我们看第二行，Use Namespaces STD 分号。
[00:05:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=309) - 注意这里有分号，它的意思是说，我们可以使用标准库中的对象和变量的名称。
[00:05:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=311) - 我们可以使用标准库中的对象和变量的名称。
[00:05:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=313) - 如果你不明白，这两句话是如何工作的，先只要把它看成几乎出现在你的任何的 C++ 程序里都可以了。
[00:05:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=315) - 第三行是一个空白行，C++ 运行的时候会忽略这行。
[00:05:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=317) - 第四行，int main()。
[00:05:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=319) - 这也是一个总出现在 C++ 程序中的东西，这是一个主函数，也叫入口函数。
[00:05:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=321) - C++ 从这里开始执行程序。
[00:05:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=323) - 它一定是要有一个大括号的，它开始执行就是大括号里面的内容。
[00:05:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=325) - 然后第五行 Cout，然后两个小于号，就代表着我要输出，输出到打印到一个命令行窗口啊，或者是文本中啊。
[00:05:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=327) - 输出的内容呢，就是双引号里面的 Hello World 的串号。
[00:05:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=329) - 注意这里要有个分号，C++ 的程序是任何语句都是以分号作为结尾的。
[00:05:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=331) - 第六行 Return 0 就说明，这个 main 函数返回值是 0，这里注意也有分号。
[00:05:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=334) - 第七行这个大括号千万不要忘了，它是一对出现的，有左边大括号就有右边大括号。
[00:05:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=336) - 好，我们来执行一下，你看，打印出来了 Hello World 的。
[00:05:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=338) - 好，我们看第二个例子，第二个例子这里就没有 Use Namespace STD 了，但是呢，我们可以这样写 STD，两个冒号，再用 Cout，也是输出，这样写也是可以的。
[00:05:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=340) - 我们运行一下，OK，也成功了。
[00:05:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=342) - 这节课我们来看 C++ 的输出，打印文本。
[00:05:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=344) - 上节课我们也讲了，Cout 这个对象再加上两个小于号，然后后面跟着双引号里面的内容 Hello World 的串号，分号，这样我们就会输出，将它输出到命令行端，或者是控制台，我们可以看一下。
[00:05:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=346) - 好，输出成功了。
[00:05:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=348) - 好，我们看下一个例子。
[00:05:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=350) - 它也可以多个输出，我们 Cout 输出一个 Hello World，再 Cout 输出一个 I'm learning C++。
[00:05:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=352) - 可以看到这里 Hello World 的串号然后连着直接输出了，这里并没有回车换行，它是挨着输出的，因为你这里没有输出回车换行符，所以它也没有。
[00:05:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=356) - 我们看下一个例子。
[00:06:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=361) - 也可以连在一起输出，我们用两个小于号先输出 Hello World 的，接着再两个小于号直接输出这句话，也是可以的。
[00:06:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=367) - 你看我们这里也是直接连着可以输出的。
[00:06:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=370) - 好，我们看第二个例子。
[00:06:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=373) - 第二个例子这里我们多了一个反斜杠 n，反斜杠 n 的意思就是换行的意思。
[00:06:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=376) - 我们来看一下。
[00:06:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=383) - 你看它就是两行。
[00:06:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=385) - 好，我们看下一个例子。
[00:06:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=391) - 这里我们输出两个反斜杠 n，也就是换两行。
[00:06:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=394) - 我们看一下，你看这里换了两行，才输出这个 I'm learning C++。
[00:06:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=399) - 这里我们输出一个。
[00:06:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=403) - ENDL，ENDL 也是回车换行的意思，这就是一个特殊标志符。
[00:06:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=407) - 我们看一眼。
[00:06:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=413) - 你看这里也换了行。
[00:06:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=418) - 好，输出讲到这里。
[00:07:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=425) - 这些课我们来看注释。
[00:07:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=429) - 注释可以用来解释 C++ 代码，并具有可读性。
[00:07:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=433) - 它也可以来测试的时候，替代码，让它阻止它执行。
[00:07:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=437) - 注释也可以是单行的或者多行的。
[00:07:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=441) - 这就是一个单行注释。
[00:07:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=443) - 单行注释就是以两个斜杠开头。
[00:07:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=452) - 后面的内容都认为是注释。
[00:07:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=454) - 同时我们也可以在这个行尾。
[00:07:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=461) - 也可以出现在这里。
[00:07:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=466) - 不一定是整行。
[00:07:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=473) - 从两个斜杠到行尾也认为是注释。
[00:07:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=476) - 前面的就不是注释。
[00:07:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=479) - 后面的这个是注释。
[00:08:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=485) - 多行注释，以斜杠星号开头。
[00:08:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=493) - 以星号斜杠结尾。
[00:08:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=500) - 两个这个之间的都认为是注释。
[00:08:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=503) - 无论它有多少行都会被编译器所忽略。
[00:08:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=508) - 我们来执行一下，你看它会输出三个 Hello World 的，但是注释并没有输出。
[00:08:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=509) - 好，大家好，这一课我们来看变量。
[00:08:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=513) - 我们来先定义一个变量。
[00:08:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=517) - 首先我们要先写 int。
[00:08:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=521) - int 的意思就是说，这个00:10:35 - 变量的类型是整形。
[00:10:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=637) - 然后这是变量的名字。
[00:10:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=638) - 买 number。
[00:10:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=640) - 买 num。
[00:10:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=641) - 然后写个等号。
[00:10:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=643) - 就是代表赋值。
[00:10:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=644) - 后面写个 15。
[00:10:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=647) - 就是说把这个 15 赋给这个变量。
[00:10:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=648) - 最后是分号结尾。
[00:10:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=655) - 然后我们来输出一下这个变量。
[00:10:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=657) - 等于 15。
[00:11:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=664) - 好，我们看另外一个例子。
[00:11:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=666) - 这里也可以一样定义变量。
[00:11:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=669) - 这里我们就是没有等号。
[00:11:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=671) - 这就代表着说这个变量是没有值的。
[00:11:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=672) - 是空值。
[00:11:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=674) - 我们还可以再下一行。
[00:11:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=676) - 然后直接给这个变量赋值。
[00:11:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=677) - 这个变量赋值的时候。
[00:11:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=678) - 就可以直接写了。
[00:11:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=680) - 买 number 等于 15。
[00:11:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=682) - 不需要整形再标示了。
[00:11:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=685) - 这个就是声明这个变量。
[00:11:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=687) - 也叫定义这个变量。
[00:11:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=690) - 后面这句话就是给变量赋值。
[00:11:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=694) - 你看一下。
[00:11:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=698) - 也是 15。
[00:11:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=704) - 好，我们看下一个例子。
[00:11:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=708) - 我们这里也是先把买 number 这个变量声明了。
[00:11:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=710) - 声明了以后给它赋了值是 15。
[00:11:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=714) - 然后我们下面这句话把它赋成 10 了。
[00:11:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=715) - 也就是说改变它的值了。
[00:11:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=716) - 改变它的值。
[00:11:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=717) - 因为变量变量。
[00:11:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=719) - 它存储的是一个值。
[00:12:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=721) - 这里 int 就代表它存储的是整形。
[00:12:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=723) - 所以你是可以改变它的值的。
[00:12:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=725) - 然后我们来把它输出出来。
[00:12:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=730) - 看一下。
[00:12:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=735) - 你看这里是 10。
[00:12:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=740) - 好，我们看下一个例子。
[00:12:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=741) - 变量有多少种类型。
[00:12:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=743) - 这里第一个是整形。
[00:12:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=745) - 我们用 int 来定义。
[00:12:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=745) - 它是整形。
[00:12:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=748) - double 就是双浮点型。
[00:12:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=750) - 双精度浮点型。
[00:12:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=752) - char 就是字符。
[00:12:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=754) - 只一个字符。
[00:12:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=756) - string 就是字符串。
[00:12:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=758) - 这是一个字符串。
[00:12:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=759) - 双引号好好引起来。
[00:12:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=761) - 布尔就是布尔类型。
[00:12:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=764) - true 或者 false。
[00:12:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=768) - 这个都是比较简单的。
[00:12:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=772) - 然后我们看下一个例子。
[00:12:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=772) - 在这里。
[00:12:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=775) - 我们可以先定义一个变量。
[00:12:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=776) - 等于 35 整形。
[00:12:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=777) - 买 a 值。
[00:12:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=779) - 然后我们可以直接输出。
[00:13:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=781) - 也是用这两个小于号。
[00:13:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=789) - 直接就把它输出来。
[00:13:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=795) - 直接 35。
[00:13:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=799) - 然后我们再来看这个例子。
[00:13:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=801) - 我们这里定义了两个变量。
[00:13:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=802) - 一个 x 等于 5。
[00:13:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=803) - 一个 y 等于 6。
[00:13:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=806) - 然后我们又定义了一个 sum 的变量。
[00:13:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=807) - 在赋值的时候。
[00:13:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=810) - 我们可以直接使用这个 x 加 y。
[00:13:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=811) - 直接就给它赋成 11。
[00:13:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=812) - 我们把它打印出来。
[00:13:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=816) - 可以看一下。
[00:13:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=818) - 你看这里出来了一个 11。
[00:13:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=820) - 因为我们输出的时候没有换行。
[00:13:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=825) - 所以直接在后面输出 11。
[00:13:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=833) - 我们看下一个例子。
[00:13:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=834) - 在定义变量的时候。
[00:13:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=835) - 我们也可以一行。
[00:13:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=836) - 定义很多个变量。
[00:13:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=839) - 我们整形 x 等于 5。
[00:14:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=840) - dou 号。
[00:14:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=841) - 这里用 dou 号分隔。
[00:14:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=844) - 其实就是 int。
[00:14:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=846) - 就是相当于分号这里。
[00:14:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=849) - int y 等于 6。
[00:14:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=850) - 再分号。
[00:14:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=851) - 然后 int z 等于 50。
[00:14:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=853) - 其实可以写来一行。
[00:14:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=854) - 用 dou 号来分隔。
[00:14:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=855) - 把三个值都给赋了。
[00:14:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=857) - 也三个 x y z。
[00:14:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=858) - 三个变量都定义好。
[00:14:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=859) - 然后我们求一下它的和。
[00:14:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=866) - 把它输出出来。
[00:14:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=870) - 可以看到这里 61。
[00:14:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=873) - 我们来看常量。
[00:14:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=873) - 常量就是不变的值。
[00:14:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=875) - 不变的值。
[00:14:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=877) - 所以它在定义变量的时候。
[00:14:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=879) - 前面加一个 const。
[00:14:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=881) - 所以 const。
[00:14:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=883) - 就代表这个值是不可变的。
[00:14:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=886) - 也就是这个 60 是不可变的。
[00:14:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=889) - 或者说这个浮点整形 。
[00:14:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=891) - 这个常量 3.14 是不可变的。
[00:14:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=894) - 我们经常会这样来定义。
[00:14:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=897) - 像每小时多少分钟。
[00:15:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=901) - 我们就会定义成一个常量。
[00:15:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=903) - 我们来看这个例子。
[00:15:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=906) - 我们把这个买。
[00:15:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=907) - num 定义成一个常量以后。
[00:15:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=910) - 然后我们又对它进行赋值。
[00:15:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=914) - 可以看到这里已经报错了。
[00:15:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=916) - 这里有引号可以看到。
[00:15:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=918) - 它永远都是 15。
[00:15:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=919) - 它不允许修改。
[00:15:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=924) - 你看我们编译。
[00:15:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=928) - 它也是通不过的。
[00:15:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=928) - 你看这里也报错了。
[00:15:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=928) - 它不能给赋值一个只读的。00:15:31 - 变量
[00:15:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=932) - 它叫只读的变量。
[00:15:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=935) - 也就是常量里面。
[00:15:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=938) - 我们来看为变量构建名称的一般规则。
[00:15:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=943) - 名称可以包含字母、数字和下划线。
[00:15:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=945) - 但名称必须以字母和下划线开头，不能以数字开头。
[00:15:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=947) - 名称是区分大小写的。
[00:15:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=949) - 你看这小写的买瓦和买瓦是不一样的，是不同的变量。
[00:15:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=953) - 名称中是不能有空格和特殊字符的。
[00:15:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=955) - 像井号、百分号这些都不行的。
[00:15:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=958) - 有一些保留字。
[00:16:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=961) - 像 C++ 里面关键字，int、stream 这些都不能作为名称来使用。
[00:16:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=964) - 大家好。
[00:16:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=970) - 这一课我们来看输入。
[00:16:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=971) - 首先我们还是引入 iostream 这个输入输出库。
[00:16:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=973) - 然后这里我们定义了一个整形的 x。
[00:16:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=979) - 首先我们 Cout 输出一个字符串。
[00:16:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=982) - Type aNumber。
[00:16:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=985) - 然后这里我们用 Cin，两个大于号 x 就表示我们从键盘读入到 x 里面。
[00:16:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=988) - 注意这里 x 的整形，所以我们只能读入数字。
[00:16:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=990) - 然后我们用 Cout 输出 yNumber 和 x。
[00:16:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=992) - 我们来运行一下。
[00:16:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=996) - 可以看到这里就等着输入。
[00:16:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=998) - 然后我们输入 5。
[00:16:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1001) - 出现了。
[00:16:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1004) - 然后我们看下一个例子。
[00:16:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1006) - 这个例子是我们先定义了 x 和 y 都是整形，然后我们又定义了一个 Sum 也是整形。
[00:16:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1009) - 我们先输出 Type aNumber。
[00:16:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1011) - 然后输入一个字符到 x 里面。
[00:16:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1013) - 再输出一个敲入一个字符串，敲入另外一个 Number。
[00:16:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1015) - 再输入一个数字到 y 里面。
[00:16:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1017) - 然后对 x 和 y 求和。
[00:16:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1019) - 求和以后，然后我们输出这和，也就是一个加法计算器。
[00:17:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1023) - 我们可以看一下。
[00:17:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1026) - 他先让输入一个 5。
[00:17:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1030) - 我们再输入一个 2。
[00:17:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1037) - 好 5 加 2 等于 7。
[00:17:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1041) - OK，输入我们就讲到这里。
[00:17:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1043) - 大家好。
[00:17:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1046) - 这节课我们来看数据类型。
[00:17:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1049) - 前面我们也看到了，这个是整形。
[00:17:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1050) - int 是整形。
[00:17:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1051) - 我们把它付给 5，然后我们把它打印出来。
[00:17:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1053) - 然后这里是浮点型。
[00:17:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1056) - float 就是可以表述在小数点的浮点型。
[00:17:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1060) - double 就是双精度浮点型，它的精度要比 float 高，就用 double 来表示。
[00:17:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1063) - float 和 double 也可以写成科学计数法。
[00:17:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1065) - 这里带个 e，e 就是 10 的多少次方。
[00:17:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1067) - 这是 10 的三次方，e4。
[00:17:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1068) - 大写 E 小写 e 都是可以的，这就代表 10 的四次方。
[00:17:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1070) - 我们把它打印出来。
[00:17:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1072) - x 就是字符型，只能表示一个字符，用单引号把它引起来，这只是一个大写的 D，这个字符，待会我们把它打印出来。
[00:17:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1074) - 这里 x 也可以写成数字，656667abc。
[00:17:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1075) - 这里就涉及到另外一个概念。
[00:17:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1077) - ASCII 表。
[00:18:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1080) - ASCII 表我们可以看一眼。
[00:18:02](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1082) - 这个就是 ASCII 表，美国标准信息交换代码。
[00:18:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1084) - 65。
[00:18:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1085) - 看这里实际上 65 代表的就是 A，66 代表的就是 B，67 代表的就是大写的 C。
[00:18:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1087) - 所以这里代表的就是大写的 abc。
[00:18:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1090) - 其实它字符和数字是共通的。
[00:18:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1095) - 然后这是布尔型。
[00:18:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1098) - 布尔型。
[00:18:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1100) - 我们设两个 ease coding 犯，把它设成 True，或者是把这个设成 False。
[00:18:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1103) - 好我们运行一下。
[00:18:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1104) - 我们可以看到，第一个是 5，对吧。
[00:18:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1105) - 这里输出的是 5。
[00:18:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1106) - 第二个，浮点型 5.99，双精度的浮点型，我们输出了 9.98。
[00:18:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1107) - 这个 35e3，也就是 10 的三次幂，也就是 35。
[00:18:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1109) - 这个 12e4 次幂，也就是 12 万。
[00:18:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1111) - 这个是字符型，输出是 D，你看这里 abc 都是大写。
[00:18:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1113) - 这里就是 656667，这是 ASCII 表决定的。
[00:18:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1115) - 这里输出的 true，true 就是 1。
[00:18:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1118) - 这里 False 就是 0。00:20:12 - 在C++里面都是这样子。
[00:20:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1215) - False就是0。
[00:20:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1219) - 好，我们看下一个。
[00:20:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1221) - 这里我们再引入一个标准库，叫String。
[00:20:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1223) - 然后我们可以直接用String来定义一个字符串变量。
[00:20:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1229) - 我们给它一个值，叫Hello，双引号引起来。
[00:20:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1234) - 双引号里面的内容是它的值，Hello是它的内容。
[00:20:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1237) - 然后我们把它打印出来，可以看一下。
[00:20:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1242) - 可以看到Hello出来了。
[00:20:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1244) - 好，这期课讲到这里。
[00:20:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1248) - 大家好，这期课我们来看运算。
[00:20:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1250) - 我们看第一个。
[00:20:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1252) - 先把x赋给5，2赋给y。
[00:20:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1255) - 然后这是加法，x加y。
[00:20:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1258) - 减法x减y。
[00:21:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1260) - 乘法是一个星号。
[00:21:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1261) - 除法是一个杠，余x除以y是多少。
[00:21:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1266) - x。
[00:21:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1267) - 然后这里加加注意，加加在后面意味着先做前面这个事。
[00:21:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1274) - Coutx，也就是把x先输出，x因为等于5，就把x输出了，然后加加就是加1，x等于x加1。
[00:21:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1283) - 那也就是说先输出5，然后x自己再加1，就变成6了。
[00:21:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1290) - 这是自加，这个加加，你看加加放前面，因为现在下面这句话执行完以后，x等于6，那是先做加加，x先等于x加1，然后变成7了，7以后，然后再输出。
[00:21:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1304) - 所以它就是输出的是7。
[00:21:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1306) - y也是一样，先输出y，y等于2，先把2输出，然后再减减，然后这个时候y等于1。
[00:21:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1315) - y等于1以后，然后执行下面这句话，执行下面这句话的时候，先减y，y等于y减1，那也就是说y这个时候等于0，然后再输出y，那就是输出0。
[00:22:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1328) - 好，我们运行一下看一下。
[00:22:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1331) - 可以看到，第一个x加y，5加2等于7，5减2等于3，5乘2等于10，5除2，这里是整数，记得这是整除，5除2等于2，5除2等于余数是1。
[00:22:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1346) - 然后x加加，看这里x加加，输出的是5，然后加加x，这里输出的是7。
[00:22:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1356) - 然后y减减，输出的是2，减减y输出的是0，因为这里y减减以后变成1了，1以后，然后再减减y，所以是0。
[00:22:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1367) - 好，我们来看第二个例子。
[00:22:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1372) - 这里复值运算，x加等3，其实就是x等于x加3，x等于x加3，那这里就是5加3等于8。
[00:23:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1385) - x减等3，就是x等于x减3，5减3等于2。
[00:23:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1391) - 乘等也就是等于x等于x乘3，5乘3，3为15。
[00:23:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1397) - 除5除3等于1，整除。
[00:23:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1401) - 下面是一样的。
[00:23:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1403) - 好，我们运行一下，可以看一下。
[00:23:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1408) - 你看x加等3等于8，x减等3等于2，乘等3等于15，整除等3等于1，与等3等于2，都是一样的。
[00:23:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1420) - 后面一货，左进右进都是一样的，与货非都是同的。
[00:23:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1427) - 好，我看第三个例子。
[00:23:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1428) - 第三个例子是比较运算符，比较运算符，x是不是等于y，x等于5，y等于2，x是不是等于，这里记住一定是两个等号，两个等号是比较，一个等号是赋值，不等是一个叹号，一个等号代表着不等，大于号、小于号、大于等于、小于等于，他00:24:13 - 我们可以看到都是不而行。
[00:24:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1455) - 0代表着False。
[00:24:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1458) - 1确实是x不等于y，所以返回是处。
[00:24:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1460) - x确实是大于y，所以返回是处。
[00:24:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1462) - x不小于y，所以返回是False。
[00:24:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1464) - x大于等于y，返回是处。
[00:24:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1467) - x小于等于y，返回是False。
[00:24:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1475) - 我们来看第四个例子。
[00:24:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1477) - 这个是与，两个这个符号是与，两个竖线是或，一个叹号就是非。
[00:24:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1485) - 这个与就是两个都为1的时候，它才为1。
[00:24:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1488) - 只要有一个为0，它就是一个为False，它整个是为False。
[00:24:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1493) - 这两个里面，只要有一个为处，它都是处。
[00:24:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1496) - 只有两个都为False的时候，它才是False。
[00:24:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1499) - 那这个非就是处，就是False，False就是处。
[00:25:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1503) - 这个我们看一下。
[00:25:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1506) - 你看。
[00:25:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1507) - 对吧。
[00:25:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1508) - 零一零。
[00:25:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1510) - 好，运算符就讲到这里。
[00:25:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1514) - 大家好。
[00:25:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1514) - 这一刻我们来看字符串。
[00:25:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1516) - 在字符串的时候，我们要引入一个字符串的库，叫String。
[00:25:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1520) - 然后我们在定义的时候，要用String，然后输入变量的名，然后给它一个值，字符串的值要用双引号引起来。
[00:25:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1531) - 我们定义两个变量，一个是FalseName，一个LastName，然后我们又定义了一个String，叫FullName。
[00:25:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1537) - FullName，我们两个字符串相连，就直接用加号，就会把两个字符串连起来。
[00:25:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1543) - 这里就直接将他们两个连起来了。
[00:25:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1546) - 然后我们将它输出。
[00:25:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1547) - 输出的时候，我们可以看到，他们两个是直接连起来的，中间是没有空格的。
[00:25:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1553) - 然后我们再看第二个例子。
[00:25:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1556) - 第二个例子，我们就直接把它加上空格。
[00:26:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1560) - 三个字符串连起来，FullName加一个空格，再加上一个LastName连起来。
[00:26:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1565) - 我们把它打印出来。
[00:26:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1567) - 或者还有一个办法，是用Append。
[00:26:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1570) - 字符串带有Append的这个方法，直接可以Append后面跟上一个LastName，这个字符串，他们两个也连起来了，和第一个效果是一样的。
[00:26:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1583) - 我们先看一下。
[00:26:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1587) - 可以看到，你看第一个连接起来了，中间是没有空格的。
[00:26:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1591) - 第二个我们这里加了一个空格，字符串，所以第三个用Append，他们之间也是没有的。
[00:26:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1599) - 然后我们定义好一个字符串，叫TSC，TSC。
[00:26:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1602) - 我们想看一下它的长度，它有两个方法，都可以，一个是Last方法，一个是Size方法，这两个都可以看到这个字符串的长度。
[00:26:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1612) - 我们可以看到这里都是26。
[00:26:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1616) - 然后我们想读取某个字符串的值，我们这里定一个叫MessDream，这个变量里面是Hello。
[00:27:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1623) - 它是从0开始，我们直接用中括号加上这个字符，就下标，从0开始，我们就可以读到这个H。
[00:27:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1633) - 如果我们想改变的话，我们直接就把下标直接给它改成J，改成J了以后，它也就变成了J楼。
[00:27:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1645) - 可以看到这里，字符串讲到这里。
[00:27:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1649) - 大家好。
[00:27:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1649) - 这期课我们来看算数。
[00:27:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1651) - 这里我们要引入一个CMess的数学库。
[00:27:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1656) - 然后我们看它有很多种函数。
[00:27:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1658) - 第一个Mess函数就比大小，最大值取最小值，5和10谁小。
[00:27:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1666) - Squad开平方。
[00:27:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1669) - Round45入。
[00:27:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1672) - Log自然对数抵达2。
[00:27:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1674) - 看日子多少。
[00:27:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1675) - 还有ABS绝对值。
[00:27:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1677) - Ack。00:28:01 - Sign, AckCosign, AckTank。
[00:28:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1683) - 这里面有很多。
[00:28:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1687) - Cosign, CosignH。
[00:28:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1689) - 这里面有很多。
[00:28:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1692) - Floor 求他的值。
[00:28:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1695) - 我们可以看到 PowerX 的 YsMe。
[00:28:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1699) - 3H, TankH。
[00:28:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1700) - 我们运行一下。
[00:28:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1705) - 我们可以看到。
[00:28:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1707) - 前面。
[00:28:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1710) - 这个 5 和 10 比大小是 10。
[00:28:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1712) - Me，这个是 5。
[00:28:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1715) - 64 的开平方是 8。
[00:28:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1717) - Round 2.63。
[00:28:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1720) - Log 2.0.69。
[00:28:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1722) - ABS 的 X 的值。
[00:28:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1723) - 这里面有很多函数。
[00:28:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1725) - 我们到时候用的时候可以直接用。
[00:28:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1730) - 好，这些可以讲到这里。
[00:28:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1732) - 好，我们接着来看条件语句。
[00:28:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1735) - 条件语句就是这个 if。
[00:28:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1737) - if 后面跟一个括号。
[00:28:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1739) - 括号里面写的是一个 True 或者 False 的表达式。
[00:29:02](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1742) - 我们可以看到 20 大于 18。
[00:29:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1744) - 确实是大于，那就是 True。
[00:29:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1746) - 如果它当为 True 的时候。
[00:29:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1748) - 那这个大括号里面的内容。
[00:29:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1751) - 这个大括号里面的内容就会被执行。
[00:29:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1754) - 这个就是条件。
[00:29:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1756) - 如果这个条件成立等于 True。
[00:29:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1758) - 那么大括号里面的就会被执行。
[00:29:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1761) - 好，我们看下面这个例子。
[00:29:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1762) - 我们把 Time 设成 20。
[00:29:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1765) - 如果 Time 小于 18。
[00:29:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1768) - 那发现这里肯定是不小于 18 的。
[00:29:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1770) - 那是 False。
[00:29:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1771) - False 这一句话就是不会去执行的。
[00:29:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1774) - 那执行什么呢。
[00:29:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1776) - 如果 if 这个不执行的话。
[00:29:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1778) - 那我们看他这里有 else。
[00:29:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1780) - 那我们就会去执行这个 else。
[00:29:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1783) - else 里面这句话。
[00:29:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1784) - 我们就会打印我的 Uni。
[00:29:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1786) - 然后我们再看下一个例子。
[00:29:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1789) - 如果 Time 小于 10。
[00:29:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1791) - 而知道是 False，不会小于 10。
[00:29:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1793) - 那它是不会执行的。
[00:29:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1794) - 那我们还可以再写 else if。
[00:29:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1797) - else if 另外一个条件。
[00:29:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1799) - Time 小于 25 吗。
[00:30:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1800) - 20 小于 25 是 True。
[00:30:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1803) - 这个是成立的。
[00:30:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1804) - 那我们就打印这个。
[00:30:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1805) - 如果 else if 执行了的话。
[00:30:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1810) - 那这个 else 就不会执行了。
[00:30:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1812) - 这个 Uni 也不会执行。
[00:30:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1814) - 当然还有一种简单写法。
[00:30:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1816) - 简单写法我们设一个 Result。
[00:30:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1818) - 等于一个什么。
[00:30:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1819) - 等于一个表达式。
[00:30:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1820) - 这个表达式是先看前面这个。
[00:30:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1823) - Time 小于 18 是 True 还是 False。
[00:30:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1827) - 这里是 False。
[00:30:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1828) - False 的话。
[00:30:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1830) - 那就会执行冒号后面的这个。
[00:30:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1832) - 把它付给猫。
[00:30:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1834) - 这个 Uni 就付给这个 Result。
[00:30:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1837) - 如果它是 True。
[00:30:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1838) - 那就是 Goodday 付给这个 Result。
[00:30:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1841) - 然后把它打印出来。
[00:30:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1842) - 好。
[00:30:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1842) - 我们执行一下看一下。
[00:30:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1846) - 看到第一个。
[00:30:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1848) - 因为 20 大于 18。
[00:30:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1850) - 所以我们就把这句话打印出来了。
[00:30:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1854) - 然后我们再看这个 20 小于 18 是 False。
[00:30:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1858) - 所以我们打印的这个 Uni。
[00:31:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1863) - 20 小于 10 是 False。
[00:31:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1866) - 20 小于 25 是 True。
[00:31:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1868) - 所以我们打印的是 Goodday。
[00:31:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1870) - 打印了 Goodday。
[00:31:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1871) - 这个 else 就不会执行了。
[00:31:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1873) - 然后这里 20 小于 18 是 False。
[00:31:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1876) - 所以 Goodday Uni 付给了 Result。
[00:31:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1879) - 所以我们把 Result 打印出来。
[00:31:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1881) - Goodday Uni。
[00:31:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1883) - 好。
[00:31:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1883) - 这几课讲到这里。
[00:31:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1886) - 大家好。
[00:31:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1887) - 这几课我们来看 Switch 语句。
[00:31:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1889) - Switch。
[00:31:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1890) - 这是关键字 Switch。
[00:31:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1892) - 然后括号。
[00:31:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1893) - 括号里面这个东西是一定要有一个值的。
[00:31:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1896) - 我们这里是一个变量。
[00:31:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1898) - Date。
[00:31:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1898) - 我们把它定义成 4。
[00:31:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1900) - 然后这里下面就是 if 的大括号。
[00:31:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1904) - 一定要有大括号。
[00:31:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1905) - 大括号里面内容。
[00:31:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1907) - 我们先写 case 1。
[00:31:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1908) - case 几都可以。
[00:31:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1910) - 这是它的值。
[00:31:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1912) - case 然后冒号。
[00:31:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1913) - 冒号后面的这两句话。
[00:31:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1915) - 就是说它要执行的。
[00:31:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1918) - 我们输出 Monday。
[00:31:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1919) - 然后 break。
[00:32:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1920) - break 是跳出的意思。
[00:32:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1923) - 也就是说这个 Date。
[00:32:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1925) - 当它等于 1 的时候。00:32:07 - 它就执行这句话。
[00:32:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1928) - 等于2的时候，执行这个，等于3执行这个，等于4执行这个，这样比 if else 写起来看起来更清晰一些，等于5就执行输出 Friday，等于6。我们可以看一下这个例子。
[00:32:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1945) - 你可以看到输出的是 Surface。好，我们看下一个例子。
[00:32:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1961) - 这里多了一个 Default，Default 的意思就是默认。如果这个值，你看 Date 值现在等于4，它既不符合这个也不符合这个，它就会走到 Default 默认来。我们可以运行一下看一下。你看走到这里了。好，Switch 我们就讲到这里。
[00:33:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=1986) - 大家好，这期课我们来看循环语句。首先我们定一个 i 等于0。这里循环有第一种，是 while 循环，while 后面跟着括号，这里是表达式。当它等于真的时候，我们就会去执行这个大括号里面的内容。因为 i 等于0，i 小于5，它是处于 while 条件，我们就会执行里面。我们把 i 输出出来，然后对 i 进行加1。记得一定要加1，如果不加1的话，那循环那永远都是0小于5，又来0小于5，无限死循环了。那我们左右，我们每次在循环一次的时候，要把这个表达式里面的 i 加1。第一次0小于5，第二次1小于5，2小于5，3小于5，4小于5，到5小于5等于 false 了，5小于5等于 false，那这个它就不执行了。这里面的就不会再执行了，所以它打印出来的是0到4。我们可以先看一下。你看啊，从0打印到4。OK。
[00:34:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2048) - 然后我们再看第二个例子。我们再把 i 赋0，do while 语句，do while 语句的意思是说，我先不管，我上来先 do，先 do，那就先输出它，先输出它，那就是 i 等于0，我直接就输出了，输出一个0，然后这里 i++，i 变成1了。那看1小于5吗？1确实小于5，true，那后来再来执行这个 do，那就输出1，然后加2小于5，然后这样输出4，2输出3，输出4，4完了加，加4加了以后等于5，5呢？5不小于5了，是 false，那这里就不执行了。注意这里，这里是一定要有个分号的，和这里是不一样的，和这个 while 语句，while 语句你看最后大括号里面是没有分号的。在这里，while 这里是一定要有一个分号存在的。我们可以看到这里输出的也是0到4。可以看到，好，我们后面继续看 for 循环。
[00:35:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2124) - 我们看第一个例子。for 这里括号，这里有两个分号分开了，三个表达式，第一个代表着 i 是初始值，这个是初始语句，我们把 i 赋成0。然后呢，这个是判断语句，i 是不是小于5，确实是小于5，i 等于0，0小于5，这是判断语句。后面这是自加语句，自加语句的意思就是说这句话执行完了以后，这里再执行这句话，执行这句话，然后再来判断这句话。你看，你说 i 等于0，等于0以后，然后输出这个0，输出这个0以后，然后 i++。00:06:06 - 也就是 i 现在等于 1。
[00:36:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2169) - 然后判断 1 是不是小于 5，是小于 5。
[00:36:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2171) - 那继续执行这句话，执行这句话，然后发现输出 1 以后，然后 1 再加，变成 2，2 是不是小于 5，2 小于 5，那执行这句话，然后执行完 i 变成 3，3 是不是小于 5，再输出 3，然后输出 4，这样子。
[00:36:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2173) - 同样呢，我们还可以这样子来写，你看 i 加加，我们还可以，这个例子，我们可以加 2，我们不加 1 了，我们可以加 2，把这个值付给 2，也就是 i 等于 0 的时候，0 小于 10，那我们输出 0，输出 0 以后，然后 0 加 2，输给 i，0 加 2，输给 i，i 变成 2 了，2 也是小于 10 的，然后就输出 2，2 了以后，然后这里 2 加 2，等于 4，4 是不是小于等于 10，是小于等于 10 了，那我们再输出 4，那这样子，一次输出，最后输出到 10。
[00:37:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2230) - 我们看下面这个例子，下面这个例子有一个 break，我们先执行，像上面这个例子，我们可以看到，这里 01234，0246810，这里，这两个例子，01234，这个 024680，好，我们看下面这个例子，下面这个例子，在这里，i 等于 0，i 小于 10，i 加加，这个都是常规的，然后这里判断，如果 i 等于 4 的时候，直接就 break 掉了，这 break 的意思是跳出整个循环，这个循环就不会再继续了，也就是说开始 i 等于 0，i 等于 0，这个不等，输出 0，i 等于 1，这个也不等，等于 i 等于 4 的时候，4 等于 4，4 等于 4 的时候，直接就 break 掉，整个循环就不再执行了，这里 4，这句话也不会执行了，然后下面等于 5 也不会执行了，i 等于 5 的时候也不会执行了，我们可以看到这里输出 0123，对吧，到 4 就是不会执行了。
[00:38:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2302) - 然后我们看 continue，主要看 break、continue 有什么不同，continue 的意思是说，i 等于 4，然后执行这句话 continue，执行 continue 的话，后面这句话就不会执行了，但是下一个循环 i 加加，i 变成 5 了，继续往下执行，也就是单单等于 4，执行到这里，后面的这些话不会执行，不是整个循环跳出，是 continue 后面的这些不会语句不会执行，单一循环的后面语句不会执行了。
[00:38:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2338) - 我们可以看到这里，你看这里 0123，这里没有 4，56789。
[00:39:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2346) - 好，循环我们就讲到这。
[00:39:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2349) - 大家好，这一刻我们来看数组，数组的话就是在这里，加上一个中括号，里面有一个 4 数值，数值的时候，就是说这是一个 4 个长的字符串数组，这里我们赋值的时候用大括号，然后中间用逗号分隔，里面是字符串，因为这里是定义的是字符串，字符串数组 pass，当然我们也可以定义一个不定长的数组，直接是中括号，这里就不写值了，后面赋值，我们这里赋了 5 个值，那00:39:44 - 它就是5个长的，大括号里面用逗号分隔。
[00:39:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2387) - 当然我们也可以定义整形数组，整形数组我们就是int。
[00:39:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2389) - 这里用中括号，就是写个3，那就是三个长的整形数组。
[00:39:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2391) - 这里也是大括号，赋值的时候也是大括号，用逗号分隔，有三个值。
[00:39:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2394) - 在输出的时候，这里我们直接也是中括号，一个下标0，那我们就输出了第一个数组。
[00:39:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2395) - 它也叫第0个数组，我们是从0开始的。
[00:39:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2397) - 然后我们对数组进行循环也是一样的，我们i从0开始，i小于4。
[00:39:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2399) - 那我们输出的时候，我们也可以直接，我们先输出下标i，然后一个冒号、空格，然后我们可以输出cast这个数组，
[00:40:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2400) - 第0个数组的值，第1个数组值，第2个，第3个。
[00:40:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2403) - 它是从0开始，一共4个，所以就是0,1,2,3。
[00:40:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2404) - 我们执行一下，可以看到这里，因为我们这里cast0是WallWall，然后我们循环，第0个WallWall，第1个BMW，第2个福特，第3个马斯达。
[00:40:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2407) - 好，数组我们就讲到这里，这些课我们来看指针和引用。
[00:40:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2411) - 我们第1个来看引用，首先我们定义一个字符串，叫Food里面的值是pisa。
[00:40:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2412) - 然后我们要看这句话，再定义一个字符串，然后这里有一个and符号，and符号跟了一个变量mail，然后指向等于什么呢，给它赋值，赋给了Food，Food里面的值就是pisa。
[00:40:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2415) - 那也就是说，这里代表说mail的地址，这个and符号就代表着mail的地址，指向了Food的值，也就是指向了pisa。
[00:40:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2417) - 也就是说pisa是内存里面的一个值，但是内存块的地址是多少呢。
[00:40:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2419) - 也就是把内存块的地址，mail的地址，它的地址指向了它的地址，指向了pisa这个地址。
[00:40:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2420) - 也就是这个像什么一样，快捷方式一样，文件里面的快捷方式，也就是它俩这两个变量，现在都指向了pisa内存块的地址。
[00:40:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2422) - Food是直接用这个赋值，然后它是把mail的地址指向了Food的这个值。
[00:40:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2423) - 我们看打印一下，你看我们打印Food的值就是pisa，打印mail的值也是pisa，说明它们俩指向了同一个内存块。
[00:40:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2425) - 然后再打印这个andFood，打印出来的就是这个Food的这个变量所在的地址，也就是这个pisa这个字符串所在的内存块的地址。
[00:40:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2427) - 我们执行一下，你看打印出来两个是pisa，这个是这个内存块所在的地址。
[00:40:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2430) - 这里一定要注意，这就叫引用，引用的意思就是说，我把mail的地址指向了Food的这个变量，也就是说它们俩是指向了同一个内存块，这样就叫引用。
[00:40:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2432) - 我们看下一个例子，指针。
[00:40:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2433) - 这里一样，我们先定义一个字符串Food的值叫pisa，然后这里String新ptr这个变量。
[00:40:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2433) - 或者说也可以这么写，String新ptr也是一样的，都是一样的写法。
[00:40:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2434) - ptr这个变量指向了什么呢，这里就好理解了，指向了Food的这个地址。
[00:40:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2435) - ptr里面的内容，它这个变量里面的内容是个地址，和前面的不一样，和前面是它的地址指向了这块内容，这两个是不同的概念。
[00:40:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2436) - 这里面的这个值，ptr里面的值是一个内存地址，就是因为这里有个星，这里有个星，所以它的值是一个地址，地址是什么呢，Food的地址。
[00:40:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2437) - 然后我们看，把这两个打印出来，把Food打印出来，把Food的地址打印出来，把ptr打印出来。00:44:08 - ptr打印出来，应该就是Food的地址。
[00:44:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2650) - 然后星ptr，这里星ptr的意思就是这个地址所在的值是啥，就是星ptr这种写法，一定要把星放在前面。
[00:44:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2664) - 我们可以先运行一下，看一下。你看前四个，第一个Food的pizza，第二个Food所在的地址，你这个ptr的值，ptr的值就是Food的地址。这个然后星ptr就是这个地址所在的这个值，是pizza，看到了，前四个。
[00:44:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2688) - 然后同时你看下面，我们同样还可以对这个指针所在的这个值，地址所在的这个负值，我们把它负成汉堡包，Hamburger。星ptr我们是可以负值的，它其实和Food是一样的。然后我们把星ptr打印出来，把Food打印出来，我们可以看到两个都是Hamburger。其实他们是指向了同一个内存地址，同一块内存内容，然后把它改成Hamburger了，那它也就变成Hamburger，Food也就变成了Hamburger。
[00:45:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2723) - 好，指针就讲到这里。
[00:45:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2726) - 大家好，这期课我们来看函数。我们先来看函数。
[00:45:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2730) - 这里函数也是要有一个类型，这个是返回类型，外的就是空，就不需要返回。看这里int就是整形，所以它就需要返回一个整数。你看这里Return一个0，然后这里My Function是函数名，然后带着括号，括号里面可以加参数，然后大括号，大括号里面内容就是函数体。可以看到这里Mate，函数名，然后一个括号，然后大括号，大括号里面，这个就是函数的内容，函数体。
[00:46:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2767) - 可以看到我们这个函数是一个返回值是一个空的函数，里面只是做了一个输出，输出了这么一句话。然后怎么调用呢？因为Mate是主函数，我们从Mate函数进来的时候调用，那就是直接写函数名，然后加上括号，加上分号，这样就会调用到函数，就会执行，执行函数，然后进来就会执行这句话，然后再执行Return。我们可以看一下。你看他输出了这句话。
[00:46:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2801) - 函数还是比较简单的，函数的功能就是把一些相同的功能，把它不用重复写多少遍，我可以调很多遍。我可以看第二个例子。你看第二个例子，这里我们把函数写在了这里，但是Mate调用的时候，如果直接这么调，假如说下面没有函数声明这句话的话，直接调它会爆错，因为它是从上往下的。所以我们要在前面先声明一下函数，声明这函数，就说不需要写这个实现，不需要写大括号里面的内容，我们只要声明这函数是空的，返回值是空，然后函数的名字，括号加上分号，这样我们就声明好了一个函数。
[00:47:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2847) - 这样我们在Mate调用的时候，我们就可以直接调用。但是它的实现，我们就要在下面来写。同样我们也是Wide，然后买方式和括号，然后这里我们再写大括号里面的内容，这样这就是它的实现，也叫它的定义，这个叫它的声明。我们运行一下看一下。你看这里也是成功的。
[00:47:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2871) - 如果我们这里不声明，还是像这样子，我们只是把Mate写前面，把Mate方式写后面，这样它会爆错的。我们可以看一下。你看这里就会爆错。00:48:08 - 它就找不到函数。
[00:48:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2888) - 好，我们看第三个例子。
[00:48:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2896) - 函数，刚才我们说，函数的功能就是这一段话，我们不用写多遍，我们可以用这个某种方式。
[00:48:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2907) - 我们这里传了一个参数，这个参数的类型是 String 类型的，叫 FName，名字叫 FName。所以我们在调用的时候，那就要把这里面传个字符串进来。你看我们这里调用了三次，调用了三次，那它就会打印三次，这个 Cout 输出三回。所以函数的功能就是相同的功能，我们把它形成一个函数，那就不用写多遍的代码。我们来运行一下，看一下，可以看到这里输出了三个，对吧。
[00:49:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2944) - 好，我们继续看。
[00:49:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2948) - 这里我们看这里，我们不光在定义这个变量的时候，我们还写了个等号，等于 Norway。等于 Norway 的意思，就是给它一个默认值。如果当我们这里不传值的时候，不传值的时候，那这个参数的值就是 Norway。如果这里我们传了值，Swedon，那它这个参数的值就是 Swedon。我们执行一下看一下，你看 Swedon, Indian, Norway, USA。这里没传值就是挪威，传值就是它的值。
[00:49:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=2983) - 好，我们看第五个。第五个如果我们有多个变量，怎么办呢？就是用逗号分割。我们第一个变量是一个字符串，ifname。第二个变量是个整形，H。然后我们把它输出出来。在传的时候一定要注意，第一个一定是传一个字符串，第二个是一个整形，这是一定要有顺序的。它的定义是什么样子，这里定义是字符串和整形，那这里传值也是字符串和整形，它是一定要有一个顺序的。我们看一下，运行一下，可以看到打印出来了三句话。
[00:50:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3023) - 好，我们看第六个。第六个这里，我们也可以直接地定义两个，我们这里定义了一个函数，这个函数是传入 X、Y 两个整形，然后把 X 加 Y 的和返回回去。然后这里我们可以直接调用，函数 5 和 3，直接这样写，括号 5 3，这样也是将 5 加 3 计算出来 8，然后输出出来。或者说我们也可以把函数 5 3 作为一个值赋给 Z，Z 也等于 8，把 Z 打出来，我们可以看一下，两个 8。
[00:50:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3059) - 好，我们看第七个例子。第七个例子，我们可以看到这里有一个 Swap1 和 Swap2，两个唯一的，里面都是一样，把 X 赋给 Z，然后 Y 赋给 X，Z 赋给 Y，相当于做了一个颠倒，中间用一个 Z，把 X 和 Y 做一个互换。但是这里有一点不同，这里声明的时候，这里的 X 是 X 和 Y 都是值，这里是 X 的地址和 Y 的地址。可以看到这两个是以用 X，以用 Y。那我们可以看一下，这两个有什么不同。我们先定义 firstNumber 的 10，secondNumber 的 20。那我们在 Swap 之前，我们打印出来，然后把这两个值打印出来。然后我们在 after 打印出来。然后我们先用 Swap1 做了互换，然后用 Swap2 做了互换，把它俩打印出来。可以看一下，可以看最开始是 10 和 20，对吧，first 是 10，second 是 20，然后 Swap1 做互换的时候，它并没有互换成功，你看 firstNumber 还是 10，secondNumber 还是 20，但是用 Swap2 的时候就互换成功了，是 20 和 10。这里有一个什么问题呢？就是在这里。00:52:23 - antX和antY。
[00:52:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3145) - 当它传值进来的时候。
[00:52:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3147) - 用Swap1传进来的时候。
[00:52:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3150) - 它只是把值传进来了。
[00:52:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3152) - X确实等于10。
[00:52:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3154) - Y确实等于20。
[00:52:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3157) - 但是它没有返回值。
[00:52:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3159) - X和Y确实也做了交换。
[00:52:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3162) - X确实变成了20。
[00:52:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3164) - Y确实变成了10。
[00:52:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3166) - 但是在这里。
[00:52:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3167) - 它只是把firstNumber赋给了X。
[00:52:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3170) - 也就是把10赋给了X。
[00:52:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3172) - firstNumber和X是指向了两块不同的内存块。
[00:52:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3176) - 但是它们的值都是10。
[00:52:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3179) - Y和second也是一样。
[00:53:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3181) - 都是指向了不同的两个内存块。
[00:53:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3183) - 它们的值都是20。
[00:53:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3185) - 所以X和Y再怎么互换。
[00:53:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3188) - 外面first和second也不会互换。
[00:53:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3191) - 但这里是把X的地址指向了first。
[00:53:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3198) - Y的地址指向了second。
[00:53:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3200) - 也就是说它们first和X是指向了同一个内存块。
[00:53:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3205) - Y和second也指向了同一个内存块。
[00:53:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3209) - 指向的是20。
[00:53:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3210) - 所以X和Y互换。
[00:53:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3212) - 也就是这两个内存块会互换。
[00:53:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3214) - 也就是说first和second这两个值也就会互换。
[00:53:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3218) - 所以这里是不一样的。
[00:53:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3221) - 这就是引用。
[00:53:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3222) - 看到了吧。
[00:53:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3223) - 引用它因为x的地址指向了first。
[00:53:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3228) - 所以它们俩指向了同一个内存块。
[00:53:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3231) - 这就是不一样。
[00:53:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3235) - 我们来看函数的重载。
[00:53:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3237) - 我们这里有两个一样的函数名。
[00:54:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3240) - plus funk。
[00:54:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3241) - 这里也是plus funk。
[00:54:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3243) - 看到但是返回值。
[00:54:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3244) - 他是int。
[00:54:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3245) - 他是double。
[00:54:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3246) - 他的参数也不一样。
[00:54:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3248) - 他的参数是intX和intY。
[00:54:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3250) - 这里是doubleX和doubleY。
[00:54:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3253) - 它里面也不一样。
[00:54:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3255) - 这个整形的是X加Y。
[00:54:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3258) - 这个是X加Y。
[00:54:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3260) - 求它的X。
[00:54:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3262) - 我们来看这里。
[00:54:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3263) - 虽然是函数名相同。
[00:54:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3265) - 但是具有相同函数名。
[00:54:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3267) - 但是功能是不一样的。
[00:54:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3269) - 这个就叫重载。
[00:54:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3272) - 这样就是为了后面方便来写。
[00:54:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3274) - 他调用的传的值。
[00:54:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3275) - 你看这里。
[00:54:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3276) - plus funk传的是8和5。
[00:54:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3280) - 传的是整形。
[00:54:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3281) - 也就是说调的是这个函数。
[00:54:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3283) - 这里传的4.3和6.26。
[00:54:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3286) - 说明他调的是这个函数。
[00:54:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3288) - 也重载的意思。
[00:54:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3290) - 也就是说多个函数名。
[00:54:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3292) - 多个函数可以具有相同的名字。
[00:54:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3295) - 但是功能和参数是不一样。
[00:54:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3297) - 由参数和功能来区分。
[00:55:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3300) - 它是不同的。
[00:55:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3301) - 你看我们执行一下。
[00:55:02](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3302) - 执行出来的是不一样的。
[00:55:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3305) - 你看第一个调用的是整形的plus funk。
[00:55:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3308) - 第二个调用的是double型的plus funk。
[00:55:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3312) - 这就是函数的重载。
[00:55:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3315) - 好函数我们就讲到这里。
[00:55:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3320) - 大家好。
[00:55:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3320) - 这一刻我们来看C++的类。
[00:55:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3323) - 什么是OP。
[00:55:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3324) - OP就是面向对象编程的意思。
[00:55:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3327) - 程序化编程。
[00:55:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3328) - 就指编写程序对数据进行。
[00:55:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3331) - 操作的程序或者函数。
[00:55:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3333) - 面向对象编程。
[00:55:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3334) - 就是同时创建数据和函数的对象。
[00:55:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3339) - 与程序编程相比。
[00:55:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3340) - 面向对象编程有几个优点。
[00:55:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3342) - 第一是更快。
[00:55:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3343) - 也更容易执行。
[00:55:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3345) - 第二他的程序结构也比较清晰。
[00:55:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3348) - 第三个他有助于保持C++代码比较干净。
[00:55:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3351) - 他不会重复自己。
[00:55:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3352) - 也更容易维护。
[00:55:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3353) - 修改和调试。
[00:55:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3355) - 他也会使用更少的代码。
[00:55:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3357) - 或者更短的开发时间。
[00:55:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3359) - 创建完全可以重复的应用程序。
[00:56:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3361) - 或者可能。
[00:56:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3363) - 什么是类和对象呢。
[00:56:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3365) - 类和对象就是面向编程的。
[00:56:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3368) - 面向对象编程的两个主要方面。
[00:56:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3371) - C++是一种面向对象编程的语言。
[00:56:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3374) - 在C++中的一切都和类对象。
[00:56:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3377) - 以及他的属性方法相关。
[00:56:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3380) - 例如在现实生活中。
[00:56:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3381) - 一辆汽车就可以看成一个对象。
[00:56:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3385) - 汽车他有属性重量。
[00:56:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3387) - 颜色以及还有方法。
[00:56:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3389) - 驾驶。
[00:56:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3390) - 刹车。
[00:56:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3391) - 所以属性和方法基本上是属于。
[00:56:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3394) - 类里面的变量和函数。
[00:56:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3396) - 这些通常被称为类的成员。
[00:56:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3399) - 类是对象的模板。
[00:56:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3402) - 就是说它是抽象的。
[00:56:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=3404) - 对象就是一个实体的真正的汽车。00:00:07 - 我们只说汽车这个概念的时候，它就是一个类。
[00:00:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=49) - 如果说某一辆汽车，它就真的是一个对象。
[00:00:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=54) - 所以我们可以看这张图，我们 class，类我们可以说是 car，就是真正的一辆汽车。
[00:00:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=59) - 它可能是 Audi、BMW、Toyota。
[00:01:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=63) - 所以类是对象的模板，对象是类的一个实例。
[00:01:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=67) - 描述汽车的时候，描述就是类。
[00:01:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=73) - 当某个对象被创建的时候，它就会继承这个类中的所有变量和功能。
[00:01:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=77) - 也就是说，真有一辆实体汽车的时候，这个汽车它就会继承这个汽车描述中的所有变量，颜色、重量、功能、刹车，还有驾驶这些。
[00:01:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=95) - 我们来看第一个例子。
[00:01:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=96) - 这里我们用一个 class 这个关键字来创建这个类。
[00:01:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=102) - 这个类叫什么？叫 car。
[00:01:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=103) - 它是分大小写的，大写 CAR。
[00:01:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=106) - 然后一定要记得用大括号括上。
[00:01:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=111) - 括号里边的内容就是类的内容。
[00:01:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=115) - 这里一定不要忘了有分号。
[00:01:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=117) - 这里对类进行声明、定义。
[00:02:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=120) - 这里是一定要有分号的。
[00:02:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=123) - 这里有一个 public，public 是访问关键字，我们在后面来讲。
[00:02:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=127) - 这里我们定义了三个变量，也叫三个属性。
[00:02:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=131) - 在类里面的变量，我们叫做属性。
[00:02:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=134) - 这里一个 brown 是 string 的，一个 model 也是 string 的，一个 year 是整形的。
[00:02:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=138) - 这个就是类的定义。
[00:02:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=142) - 类的定义。
[00:02:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=145) - 然后我们怎么来声明类的对象呢？
[00:02:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=148) - 我们创建一个类的对象的时候，跟创建一个变量差不多。
[00:02:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=153) - 我们用类的名字 CAR，然后后面跟上一个变量名，然后一个分号。
[00:02:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=158) - 这样我们就创建了一个对象。
[00:02:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=161) - 有点像创建变量一样，但是类的变量就叫对象，或者叫实例。
[00:02:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=166) - 这个 CAR object1。
[00:02:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=169) - 然后我们访问属性的时候，就要用点。
[00:02:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=173) - 用点就可以访问到对象里面的属性。
[00:02:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=178) - 类是不能直接调用的。
[00:03:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=181) - 类大家记得，因为类它只是一段描述，它并没有真正的分配内存。
[00:03:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=187) - 只有在这里定义实例，或者定义对象的时候，它才真正的分配了一块内存给它。
[00:03:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=192) - 分配了一块内存给它，那它就是一个空字符串，空的字符串，然后空的一个整形。
[00:03:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=197) - 这里面是没有放东西的。
[00:03:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=201) - 在这里我们给它赋了一个值，Brown 的。
[00:03:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=205) - 这个 Object1 的 Brown 的赋了一个值。
[00:03:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=208) - Object1 的 Model 给它赋了一个值。
[00:03:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=211) - Model Object1 的 Year 给它赋了一个值。
[00:03:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=214) - 这个内存块，这个内存块里面都给它赋好值了。
[00:03:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=220) - 这新生成了一个内存块。
[00:03:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=222) - 然后我们再创建一个 2 对象，KarObject2。
[00:03:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=226) - 这也是新生成了一个内存块。
[00:03:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=229) - 这个内存块是可以给它进行复制的。
[00:03:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=232) - 直接复制类是不行的。
[00:03:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=234) - 类因为现在是一个描述，一个虚的东西，实例实体对象才能给它复制。
[00:04:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=241) - 我们访问，那就直接可以用 Object1.Brown 的，就可以访问到了。
[00:04:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=246) - KarObject1.Model 也可以直接访问了。
[00:04:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=249) - 那我们可以直接访问类点它，那是不行的。
[00:04:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=253) - 因为它只是一段描述，它只是一个描述而已，并没有真正的分配内存。
[00:04:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=260) - 我们运行一下看一下，可以看到把它都打印出来了，中间有空格分隔。
[00:04:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=267) - 好，我们来看第二个例子。
[00:04:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=269) - 第二个例子，我们来看类里面的函数。
[00:04:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=273) - 你看到这里也叫方法，在类里面的函数叫方法。
[00:04:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=276) - 看这里我们定义两个函数，一个叫 Speed 的函数，返回是整型，有一个参数是 MaxSpeed。
[00:04:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=284) - 然后还有一个空函数。00:00:46 - 叫MyMatter的。
[00:01:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=60) - 输出一个HelloWare的这句话。
[00:01:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=61) - 但是这里这个函数是没有定义的。
[00:01:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=64) - 你只有定义没有实现。
[00:01:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=66) - 那我们在下面来写实现。
[00:01:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=68) - 怎么来写呢。
[00:01:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=60) - 现在声明它是int整形。
[00:01:02](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=62) - 然后ha这个类名。
[00:01:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=64) - 两个帽号。
[00:01:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=65) - 然后写这个方法名称。
[00:01:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=69) - 然后这里扩号参数。
[00:01:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=73) - 然后这里来写实现。
[00:01:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=74) - 直接返回它的最大。
[00:01:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=76) - MaxSpeed的返回。
[00:01:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=78) - 然后我们来看。
[00:01:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=79) - 这里先声明一个对象。
[00:01:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=81) - 叫MyObject。
[00:01:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=82) - MyObject。
[00:01:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=83) - 然后直接输出。
[00:01:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=85) - MyObject的函数。
[00:01:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=86) - 函数也是点。
[00:01:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=87) - 点Speed的200。
[00:01:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=89) - 那它这里直接返回。
[00:01:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=90) - 那应该是输出200。
[00:01:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=93) - 然后再看这个。
[00:01:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=94) - 我们再调用MyObject的点。
[00:01:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=96) - MyMatter的点。
[00:01:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=97) - MyMatter的。
[00:01:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=99) - 因为它是一个空函数。
[00:01:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=100) - Ware的空函数。
[00:01:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=102) - 但是它执行这句话。
[00:01:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=103) - Sealout直接输出HelloWare的。
[00:01:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=105) - 所以它也会打印出HelloWare的。
[00:01:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=107) - 我们执行一下。
[00:01:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=108) - 看一下。
[00:01:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=109) - 你看这里200。
[00:01:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=110) - HelloWare的。
[00:01:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=113) - 好。
[00:01:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=113) - 我们来看第三个例子。
[00:01:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=116) - 第三个例子。
[00:01:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=117) - 这里有一个跟类名相同的一个函数。
[00:02:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=120) - 可以看到这里也没有返回值。
[00:02:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=123) - 也没有什么整形。
[00:02:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=124) - intWare的返回值。
[00:02:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=126) - 这里直接就写卡扩号。
[00:02:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=129) - 然后这里传了三个函数。
[00:02:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=132) - 两个Stream。
[00:02:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=133) - XY。
[00:02:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=134) - 一个NTZ。
[00:02:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=136) - 这个函数就叫构造函数。
[00:02:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=138) - 因为它和类名相同。
[00:02:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=141) - 为什么叫构造函数。
[00:02:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=142) - 就是在这里创建这个对象的时候。
[00:02:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=149) - 它这个函数就会被执行。
[00:02:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=152) - 这个函数就会被执行到。
[00:02:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=154) - 所以在创建对象的时候。
[00:02:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=156) - 就必须要传入三个参数。
[00:02:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=159) - 因为它这里有三个参数。
[00:02:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=160) - 两个Stream。
[00:02:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=161) - 一个NT。
[00:02:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=162) - 所以它叫构造函数。
[00:02:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=163) - 在创建对象的时候被执行。
[00:02:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=166) - 它就叫构造函数。
[00:02:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=168) - 它只要一创建对象。
[00:02:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=169) - 它就会执行这个函数。
[00:02:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=171) - 这就是构造函数。
[00:02:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=172) - 构造函数。
[00:02:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=173) - 我们来看它我们实现。
[00:02:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=175) - 也是卡帽号然后卡。
[00:02:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=177) - 然后我们把它付给了它的属性。
[00:03:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=180) - Brund。
[00:03:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=180) - X付给Brund。
[00:03:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=181) - Y付给Model。
[00:03:02](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=182) - Z付给Yer。
[00:03:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=183) - 这样我们在创建它的时候。
[00:03:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=187) - 传入的是BMWXS1999。
[00:03:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=190) - 那它的可以看到它的Brund。
[00:03:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=194) - 那就是BMW。
[00:03:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=195) - 它的Model因为才是Y。
[00:03:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=197) - YXS。
[00:03:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=198) - 那就Model也是Y。
[00:03:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=200) - 然后Eer就是1999。
[00:03:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=202) - 因为它在创建的时候。
[00:03:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=204) - 就给这三个值复职了。
[00:03:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=206) - 三个属性复职了。
[00:03:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=207) - 那下面是福特Muston和1969。
[00:03:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=210) - 我们来执行一下。
[00:03:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=211) - 你看把它输出打印一下。
[00:03:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=213) - 可以看到。
[00:03:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=217) - 可以看到。
[00:03:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=218) - 好。
[00:03:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=221) - 好。
[00:03:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=221) - 我们继续看下一个例子。
[00:03:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=223) - 这里你看我们这里intB是没有范围的。
[00:03:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=227) - 这里Public。
[00:03:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=228) - 这是有一个Public。
[00:03:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=230) - 有设了一个X和Y。
[00:03:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=232) - 这里一个Private设了一个A。
[00:03:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=235) - 我们来说一下Public和Private。
[00:03:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=238) - 这就是C++里面类的访问范围。
[00:04:02](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=242) - Public里面的成员像这X和Y。
[00:04:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=245) - 外部的变量是可以访问到的。
[00:04:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=248) - PrivateA或者是B。
[00:04:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=251) - 如果B不写。
[00:04:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=253) - 默认的话。
[00:04:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=254) - 它也是私有范围。
[00:04:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=257) - 我们来看A和B都是私有范围。
[00:04:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=262) - 我们看这个。
[00:04:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=263) - 我们先定义MyClass点MyObject。
[00:04:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=265) - MyObject的X等于25。
[00:04:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=268) - 这个是允许访问的。
[00:04:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=270) - 因为它是在Public的。
[00:04:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=271) - 它是公有范围的。
[00:04:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=273) - 但是MyObject点A付给50。
[00:04:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=276) - 但这里它就报了一个错。
[00:04:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=277) - 它说到它是私有属性。
[00:04:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=281) - Private tribute。00:00:00 - 因为它A是私有属性。
[00:01:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=64) - 如果我们这里再写一个MyObject点B，
[00:01:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=65) - 等于11。
[00:01:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=66) - 可以看到它也报错了。
[00:01:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=67) - 它也是一个私有属性。
[00:01:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=68) - 也是不允许访问的。
[00:01:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=69) - 所以默认都是Private的。
[00:01:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=70) - 只有Public是允许访问的。
[00:01:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=71) - 当然还有一种是Protected。
[00:01:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=72) - Protected是继承里面的。
[00:01:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=73) - 子类可以访问。
[00:01:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=74) - 所以我们在下面继承会讲到。
[00:01:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=75) - 我们再看下面这个例子。
[00:01:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=76) - 我们为了保证它的封闭性，
[00:01:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=77) - 也就是说敏感，
[00:01:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=78) - 封闭性就是指敏感的数据，
[00:01:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=79) - 不想被用户发现，
[00:01:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=80) - 或者被用户来修改。
[00:01:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=81) - 像Salary，
[00:01:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=82) - Icon整形的Salary，
[00:01:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=83) - 我们就给它设成Private的类型。
[00:01:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=84) - 外面是访问不到的。
[00:01:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=85) - 但是如果外面也想用，
[00:01:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=86) - 也想做修改，
[00:01:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=87) - 或者说访问的时候怎么办呢？
[00:01:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=88) - 我们这里设了两个方法。
[00:01:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=89) - 一个是SetSalary，
[00:01:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=90) - 一个方法。
[00:01:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=91) - 我们给一个S，
[00:01:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=92) - 然后把S付给Salary。
[00:01:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=93) - 还有一个GetSalary方法。
[00:01:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=94) - 我们返回Salary的值。
[00:01:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=95) - 这样我们通过两个公开的方法，
[00:01:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=96) - 我们就可以访问私有属性的这个值了。
[00:01:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=97) - 这样做的好处，
[00:01:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=98) - 主要还是为了保护这个数据。
[00:01:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=99) - 因为在这个方法里面，
[00:01:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=100) - 我们不仅仅是赋值，
[00:01:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=101) - 或者不仅仅是返回，
[00:01:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=102) - 我们还可以做一些其他的。
[00:01:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=103) - 假如说我们把它返回成Stream类型，
[00:01:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=104) - 或者把它是不是零判断一下，
[00:01:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=105) - 或者怎么样的，
[00:01:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=106) - 修复啊怎么样的，
[00:01:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=107) - 我们做一些合法性校验，
[00:01:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=108) - 经常会在SetSalary或者Get里面做。
[00:01:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=109) - 所以我们可以看到，
[00:01:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=110) - 我们先定义这个实力，
[00:01:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=111) - Inploy，
[00:01:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=112) - 类名，
[00:01:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=113) - 然后叫MyObject这个实力。
[00:01:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=114) - MyObject点SetSalary。
[00:01:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=115) - 我们设成5万，
[00:01:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=116) - 工资是5万。
[00:01:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=117) - 然后我们输出，
[00:01:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=118) - 直接用GetSalary来输出。
[00:01:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=119) - 我们看一下这个例子。
[00:02:00](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=120) - 你看这里输出到5万了。
[00:02:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=121) - 好。
[00:02:02](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=122) - 我们继续来看类的继承。
[00:02:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=123) - 在C++中可以将属性和方法，
[00:02:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=124) - 从一个类继承到另外一个类，
[00:02:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=125) - 这就是类的继承的概念。
[00:02:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=126) - 所以我们就可以有子类和父类的概念。
[00:02:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=127) - 我们这里定一个WorCo这个类。
[00:02:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=128) - WorCo这个类里面有一个Brown的。
[00:02:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=129) - 我们给它设一个Fold的。
[00:02:10](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=130) - 还有一个方法，
[00:02:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=131) - Honk输出一个字幕券，
[00:02:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=132) - Tutu。
[00:02:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=133) - 然后我们这里定一个子类，
[00:02:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=134) - ClassCard，
[00:02:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=135) - 然后这里冒号PublicWorCo。
[00:02:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=136) - 也就是说，
[00:02:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=137) - 我从这个WorCo来，
[00:02:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=138) - 父类来继承。
[00:02:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=139) - 继承到哪呢？
[00:02:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=140) - 继承到在Card里面，
[00:02:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=141) - 也就是这Card可以有这个属性，
[00:02:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=142) - 也有这个方法。
[00:02:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=143) - 同时它还有自己的一个属性，
[00:02:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=144) - 叫Model。
[00:02:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=145) - 我们来看把Card创建一个对象，
[00:02:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=146) - 叫MyCard。
[00:02:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=147) - MyCard就可以访问这个，
[00:02:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=148) - 他父类里面的这个方法Honk，
[00:02:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=149) - 然后也可以输出，
[00:02:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=150) - 父类的品牌Bound和他自己的属性Model。
[00:02:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=151) - 我们来运行一下，
[00:02:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=152) - 看一下。
[00:02:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=153) - 这个就是继承。
[00:02:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=154) - 你看这个都输出出来了。
[00:02:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=155) - 继承有一个好处，
[00:02:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=156) - 这样的话，
[00:02:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=157) - 我可以再进一步的抽象。
[00:02:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=158) - 细车，
[00:02:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=159) - 我可以抽象成车辆，
[00:02:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=160) - 那我这边还可以把它变成一个火车，
[00:02:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=161) - 是吧？
[00:02:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=162) - 火车来继承它。
[00:02:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=163) - 细车底下我还可以继承，
[00:02:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=164) - 某些什么样的SV细车，
[00:02:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=165) - 轿车这样子。
[00:02:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=166) - 不断的来抽象，
[00:02:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=167) - 一层一层的。
[00:02:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=168) - 我们来看下一个例子。
[00:02:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=169) - 在继承的时候，
[00:02:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=170) - 我们这里创建一个父类。
[00:02:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=171) - 这个父类里面有一个函数叫，
[00:02:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=172) - 买方式，
[00:02:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=173) - 他输出一句话。
[00:02:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=174) - 然后呢，
[00:02:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=175) - 我再定义另外一个父类，
[00:02:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=176) - 买Azure，
[00:02:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=177) - 方式也输出一句话。
[00:02:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=178) - 那我这一01:08:40 - 个子类呢。
[01:08:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4120) - 这一个子类，class my child class。
[01:08:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4123) - 这个子类。
[01:08:45](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4125) - 那我同时继承两个父类。
[01:08:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4127) - 这里看清楚。
[01:08:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4129) - public my class。
[01:08:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4130) - doher public my other class。
[01:08:53](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4133) - 所以这里一定是两个 public。
[01:08:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4136) - 都号分割的。
[01:08:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4138) - 继承下来以后呢，当然它里面没有自己的属性和方法。
[01:09:02](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4142) - 没关系。
[01:09:02](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4142) - 我们就主要是看多继承。
[01:09:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4144) - 这种就叫多继承。
[01:09:08](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4148) - 这个孩子这个类呢，继承了等于是可以继承父亲，也可以继承母亲。
[01:09:13](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4153) - 同样继承他们两个的方法。
[01:09:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4155) - 然后呢，实现这个对象。
[01:09:18](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4158) - 买 Object。
[01:09:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4160) - 那买 Object 也可以调这个买方式，也可以调这个买 Azure 方式。
[01:09:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4163) - 我们来看一下。
[01:09:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4165) - 你看两句话都输出了，this one is pyrenclass and anotherclass。
[01:09:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4175) - 好。
[01:09:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4175) - 我们看下一个例子。
[01:09:37](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4177) - 这个例子里面呢，我们先看一个积类。
[01:09:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4178) - 这个积类呢，这里有一个 protected。
[01:09:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4180) - protected。
[01:09:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4182) - 我们上面说，只有子类，这里面的这个变量，是只有子类能访问的。
[01:09:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4187) - 也就是说你看这里，我们进一个 class program，继承了这个 employee 这个类。
[01:09:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4194) - 继承了 impleee 这个类呢，它呢，在这里面，你看就可以使用这个 salary。
[01:09:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4199) - 如果这里是 private，私有的，那不好意思，这个 program 也是不能用的。
[01:10:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4206) - 只能 impleee 自己用。
[01:10:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4212) - 所以你看它这里有两个方法，public 的方法，set salary 和 get salary。
[01:10:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4216) - 也可以直接对父类里面的 salary 属性，直接进行复制，或者直接返回操作。
[01:10:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4223) - 我们可以看一下，先对 program 创建一个对象，my object。
[01:10:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4229) - my object 直接调用这个方法，set salary 给设置一个 5 万，然后又给他自己的一个属性 bonus 设了一个 1 万 5。
[01:10:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4239) - 然后我们把它打印出来，salary 冒号，把这个 get salary 打出来，然后 bonus 把这 bonus 打出来。
[01:10:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4246) - 可以看到，都打出来了。
[01:10:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4251) - 好。
[01:10:52](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4252) - 类我们就讲到这里。
[01:10:56](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4256) - 大家好，这期课我们来看多态性。
[01:10:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4257) - 多态性的意思，就是多种形式。
[01:10:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4259) - 它发生在我们许多类通过继承，而得到相互关联的时候。
[01:11:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4263) - 就像我们上一张规定的那样，继承是让我们从另一个类中，继承了它的属性和方法。
[01:11:09](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4269) - 多态性就是使用这些方法，来执行不同的任务。
[01:11:14](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4274) - 这样可以使得我们以一个不同的方式，来执行一个单一的操作。
[01:11:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4279) - 我们举个简单例子，就是说我们这里有一个 animal 的积类。
[01:11:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4282) - 它下面有一个方法叫 animal sound。
[01:11:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4286) - 也就是动物的叫。
[01:11:29](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4289) - 我们还可以做一些子类，猪、猫、狗、鸟。
[01:11:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4293) - 但是他们都有不同的叫声。
[01:11:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4295) - 名字也叫 animal sound。
[01:11:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4298) - 但是它里面的实现，猪是猪的叫声，猫是猫的叫声。
[01:11:43](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4303) - 我们看实际例子。
[01:11:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4310) - 你看我们这里，首先我们定义了一个 animal 的积类，然后我们实现了一个方法，直接输出一句话。
[01:11:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4317) - 然后我们定义了一个 peak，来继承 animal。
[01:12:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4325) - 继承 animal 是同样的，我们这里一模一样的方法，但是这里面的实现内容是不同的。
[01:12:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4332) - 你看这里输出 the pig says。
[01:12:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4337) - 然后我们再实现一个 dog，也是继承 animal。
[01:12:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4339) - 然后这里是 the dog says。
[01:12:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4342) - 方法也是一样的。
[01:12:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4344) - 这里我们出实话实例。01:12:27 - 有出实话好三个对象。
[01:12:28](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4348) - 然后分别调用 animal sound。
[01:12:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4351) - 我们来看一下。
[01:12:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4355) - 你看调用出来的都是不同的。
[01:12:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4359) - 虽然名字相同，但是它其实都是调用自己的。
[01:12:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4360) - 这就是多态。
[01:12:46](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4366) - 大家好。
[01:12:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4367) - 我们看第18节文件的读写。
[01:12:50](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4370) - 在文件读写的时候，我们要引入一个标准库叫 fstream。
[01:12:55](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4375) - 一定要引入这个 fstream 来读写文件。
[01:12:58](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4378) - 首先我们定一个 ofstream，就是输出。
[01:13:01](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4381) - 然后我们先定一个文件，文件名就是 filename.txt。
[01:13:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4385) - 给它一个 myfile 对象。
[01:13:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4391) - 我们创建一个文件，这是一个空文件，用 ofstream 来创建。
[01:13:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4395) - 创建了以后，我们就用大括号像 cout 一样输出。
[01:13:20](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4400) - 把它就输出，这句话就输出到 myfile 里面去了。
[01:13:24](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4404) - 最后一定要记得对这个文件进行关闭。
[01:13:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4407) - 你看我们执行一下。
[01:13:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4411) - 你看这里就执行成功了。
[01:13:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4413) - 我们可以看到，这里就有一个这个文件。
[01:13:35](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4415) - 你看这里这句话，写到这个文件里面了。
[01:13:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4421) - 好。
[01:13:41](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4421) - 我们来看文件的读写。
[01:13:42](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4422) - 文件读写同样是引入 fstream 标准库。
[01:13:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4427) - 引入来以后，我们先定一个字符串。
[01:13:49](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4429) - 这里我们要用 ifstream，我们因为要读取这个文件，就是 in ifstream。
[01:13:57](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4437) - 然后我们定一个变量叫 myfile。
[01:13:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4439) - 然后同样读取这个 txt 文件。
[01:14:03](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4443) - 然后读的时候，我们用 getline 这个函数。
[01:14:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4446) - getline 这个函数，首先先传入文件对象，然后把它读到哪个 stream 里面去。
[01:14:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4452) - 它是一行一行读。
[01:14:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4455) - 然后我们用 cout 把它输出出来。
[01:14:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4457) - 最后也要记得文件是一定要关闭的。
[01:14:21](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4461) - 我们运行一下看一下。
[01:14:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4465) - OK。
[01:14:25](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4465) - 成功了。
[01:14:30](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4470) - 我们看第19节异常。
[01:14:32](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4472) - 程序员在写程序的时候，会有一些程序编码错误。
[01:14:38](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4478) - 或者说在网络请求的时候有可能超时，或者在访问文件的时候，有可能文件不存在。
[01:14:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4484) - 所以它会抛出一些异常。
[01:14:47](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4487) - 我们就要捕捉这种异常来进行处理。
[01:14:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4491) - 因为它是不可控的，有可能这种错误那种错误。
[01:14:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4494) - 所以我们就需要使用 try 和 catch 这种模式。
[01:14:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4499) - try 里面我就要写，假如说我读取某个文件，或者我写文件。
[01:15:04](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4504) - 写文件的时候磁盘满了，是吧？
[01:15:06](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4506) - 或者请求某个网络响应超时了。
[01:15:11](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4511) - 那我都在 try 里面来写有可能发生的异常。
[01:15:15](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4515) - 就在 try 里面来写，然后如果发生了异常以后怎么处理，我们就在 catch 这里面来写。
[01:15:19](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4519) - 那我们看这个简单的例子。
[01:15:23](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4523) - 这个简单的例子是说，我们定一个 a 值等于 15。
[01:15:26](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4526) - 如果它大于 18 的话，那它就应该是输出一句话。
[01:15:31](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4531) - 如果不大于 18，那我们就要抛出一个异常。
[01:15:34](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4534) - 死肉。
[01:15:36](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4536) - 例子一般来说，这里面不会有死肉的。
[01:15:39](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4539) - 某个函数里面才会有死肉。
[01:15:44](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4544) - 然后我调网络函数调请求的时候，那里面可能超时了，死肉出去。
[01:15:48](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4548) - 或者说不存在了，我把它死肉出去。
[01:15:51](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4551) - 然后我们例子里面，我们就死肉一个整形出来。
[01:15:54](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4554) - 在 catch 的时候，因为它这里是个整形，所以我们 catch int。
[01:15:59](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4559) - 然后给一个变量，到时候死肉出来的变量的值就会放到这里面。
[01:16:05](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4565) - 然后我们就输出这两句话。
[01:16:07](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4567) - 我们可以看一下这个例子。
[01:16:12](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4572) - 你看这里输出了 a 值等于 15。
[01:16:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4576) - 好。
[01:16:16](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4576) - 我们看下面这个例子。
[01:16:17](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4577) - 下面这个例子同样也是死肉 505，但是这里 catch 不一样。
[01:16:22](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4582) - 开始是三个点，三个点的意思是说，那我就要把所有异常都捕获出来。
[01:16:27](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4587) - 我不管它是整形的异常，或者是其他类型的异常，我都要捕获出来。
[01:16:33](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4593) - 你看这里，它就直接也输出了这句话，就是。01:16:38 - 所有异常补和。
[01:16:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4600) - 就是三个点。
[01:16:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4600) - 好。
[01:16:40](https://www.bilibili.com/video/BV15Y411j7JW/?vd_source=ff6ba8822972c71022ac4e13df45bda2&t=4600) - 这一句话讲到这里。

## ✨ AI 润色精校版

大家好，今天我们用100分钟左右的时间来学习C++。

什么对C++呢HEAD

C++对一种跨平台的语言。

可以用于创建高性能的应用程序。

C++对由Bjarne这哥们儿开发的。

作为C语言的一个扩展。

C++同时为程序员也提供了对系统资源和内存的高度控制。

该语言在11年、14年、17年进行了三次大的变更。

即C++11、C++14和C++17。

为什么使用C++呢HEAD

因为C++对世界上最流行的语言之一。

在今天的操作系统，包括图形界面，还有一些嵌入式系统中，都可以看得见C++的身影。

C++作为一种面向对象的编程语言，它为程序员提供了清晰的结构，也便于复用，所以降低了开发成本。

同时C++也具有可移植性，开发以后可以使用于各个多平台的应用程序。

C++也比较有趣，也比较好学。

由于C++和C语言比较接近，所以程序员也很容易从C++转到C语言，反之也对一样的。

好，我们今天学习的主要内容有第一语法，输出、注释、变量，输入、数据类型，运算、字符串，条件语句、switch，循环语句，数组、指针，函数、类，多态性、文件和异常处理。

首先我们来看C++开发环境的安装。

我们首先打开MinGW的官网。

MinGW-W64.org。

然后我们去点Download。

我们可以看到，它这里对支持Windows的。

这里有个Source，Source里面，它这里有个Source Folder。

我们点击这个Source Folder。

我们看到这里直接有下载，但我们先不要下它，我们往下拉。

这里有一个MinGW的Online的安装包。

我们点击下载它。

我们可以看到这里下载完成。

我们点击打开。

然后这里版本我们可以不用管它。

这里架构，我们对X86 64位的，线程对W32的，异常处理我们可以选SEH。

这个目录我们也可以不用管，就让它安装到这里，当然你也可以自己改目录。

这样就开始安装了。

我们点下一步。

这样就安装完成了。

然后我们打开这个安装目录。

我们找到这个bin目录。

我们把这个地址复制下来。

然后我们打开计算机属性。

环境变量里面，系统变量里面的Path。

然后我们在这里添加进来。

确定。

再确定。

我们打开个命令窗口。

我们运行GCC。

然后这里直接就有下载Windo
ws的。

我们点击。

下载成功我们直接点击安装。

然后它会弹出这么一个警告。

我们可以直接点确定。

然后点我同意协议。

下一步。

这里可以选下安装目录。

它默认安装在这里。

再点下一步。

然后再点下一步。

开始安装。

安装完成。

我们打开Visual Studio Code。

这个按钮。

这个就是一层Sense。

然后我们在这里输入C++。

它就会查出来。

第一个就是这个图标。

然后我们点击安装。

这样就可以安装成功了。

好，我们来看C++的语法。

这是一个标准的C++程序。

我们看第一行。

警号Include。

尖括号IOStream。

尖括号。

IOStream是一个头文件库。

它让我们与输入输出的对象一起工作。

它让我们与输入输出的对象一起工作。

例如第

五行的 cout。

例如第五行的 cout，就可以使用这个。

我们看第二行，using namespace std 分号。

注意这里有分号，它的意思是说，我们可以使用标准库中的对象和变量的名称。

我们可以使用标准库中的对象和变量的名称。

如果你不明白，这两句话是如何工作的，先只要把它看成几乎出现在你的任何的 C++ 程序里都可以了。

第三行是一个空白行，C++ 运行的时候会忽略这行。

第四行，int main()。

这也是一个总出现在 C++ 程序中的东西，这是一个主函数，也叫入口函数。

C++ 从这里开始执行程序。

它一定是要有一个大括号的，它开始执行就是大括号里面的名称。

然后第五行 cout，然后两个小于号，就代表着我要输出，输出到打印到一个命令行窗口啊，或者到文本中啊。

输出的内容呢，就是双引号里面的 Hello World 的串号。

注意这里要有个分号，C++ 的程序是任何语句都是以分号作为结尾的。

第六行 return 0 就说明，这个 main 函数返回值是 0，这里注意也有分号。

第七行这个大括号千万不要忘了，它是成对出现的，有左边大括号就有右边大括号。

好，我们来执行一下，你看，打印出来了 Hello World 的。

好，我们看第二个例子，第二个例子这里就没有 using namespace std 了，但是呢，我们可以这样写 STD，两个冒号，再用 cout，也是输出，这样写也是可以的。

我们运行
一下，OK，也成功了。

这节课我们来看 C++ 的输出，打印文本。

上节课我们也讲了，cout 这个是象再加上两个小括号，然后后面跟着双引号面临的名称 Hello World 的叹号，分号，这样我们就会输出，将它输出到命令行端，或者是控制台，我们可以看一下。

好，输出成功了。

好，我们看下一个例子。

它也可以多个输出，我们 cout 输出一个 Hello World，再 cout 输出一个 我'm learning C++。

可以看到这里 Hello World 的叹号然后连着直接输出了，这里并没有回车换行，它是挨着输出的，因为你这里没有输出回车换行符，所以它也没有。

我们看下一个例子。

也可以连在一起输出，我们用两个小括号先输出 Hello World 的，接着再两个小括号直接输出这句话，也是可以的。

你看我们这里也是直接连着可以输出的。

好，我们看第二个例子。

第二个例子这里我们多了一个反斜杠 n，反斜杠 n意思就是换行的意思。

我们来看一下。

你看它就是两行。

好，我们看下一个例子。

这里我们输出两个反斜杠 n，也就是换两行。

我们看一下，你看这里换了两行，才输出这个 我'm learning C++。

这里我们输出一个 endl，endl 也是回车换行的意思，这就是一个特殊标志符。

我们看一眼，你看这里也换了行。

好，输出讲到这里，这些课我们来看注释。

注释可以用来解释 C++ 代码，并具有可读性。

它也可以来测试的时候，替代码，让它阻止它执行。

注释也可以对单行的或者多行的。

这就是一个单行注释，单行注释就是以两个斜杠开头，后面的名称都认为是注释。

同时我们也可以在这个行尾，也可以出现在这里，不一定是整行，从两个斜杠到行尾也认为是注释，前面的就不是注释，后面的这个是注释。

多行注释，以斜杠星号开头，以星号斜杠结尾，两个这个之间的都认为是注释，无论它有多少行都会被编译器所忽略。

我们来执行一下，你看它会输出三个 Hello World 的，但是注释并没有输出。

好，大家好，这一课我们来看变量。

我们来先定义一个变量。

首先我们要先写 int，int 的意思就是说，这个

变量的类型是整型。

然后这是变量的名字。

买 number。

买 num。

然后写个等号。

就是代表赋值。

后面写个
 15。

就是说把这个 15 赋给这个变量。

最后是分号结尾。

然后我们来输出一下这个变量。

等于 15。

好，我们看另外一个例子。

这里也可以一样定义变量。

这里我们就是对没有等号。

这就代表着说这个变量是没有值的。

是空值。

我们还可以再下一行。

然后直接给这个变量赋值。

这个变量赋值的时候。

就可以直接写了。

买 number 等于 15。

不需要整形再标示了。

这个就是声明这个变量。

也叫定义这个变量。

后面这句话就是给变量赋值。

你看一下。

也是 15。

好，我们看下一个例子。

我们这里也是先把买 number 这个变量声明了。

声明了以后给它赋了值是 15。

然后我们下面这句话把它赋成 10 了。

也就是说改变它的值了。

改变它的值。

因为变量变量。

它存储的是一个值。

这里 int 就代表它存储的是整形。

所以你是可以改变它的值的。

然后我们来把它输出出来。

看一下。

你看这里是 10。

好，我们看下一个例子。

变量有多少种类型。

这里第一个是整形。

我们用 int 来定义。

它是整形。

double 就是双浮点型。

双精度浮点型。

char 就是字符。

只一个字符。

string 就对字符串。

这是一个字符串。

双引号好好引起来。

布尔就是布尔类型。

true 或者 false。

这个都是比较简then。

然后我们看下一个例子。

在这里。

我们可以先定义一个变量。

等于 35 整形。

买 a 值。

然后我们可以直接输出。

也是用这两个小括号。

直接就把它输出来。

直接 35。

然后我们再来看这个例子。

我们这里定义了两个变量。

一个 x 等于 5。

一个 y 等于 6。

然后我们又定义了一个 sum 的变量。

在赋值的时候。

我们可以直接使用这个 x 加 y。

直接就给它赋成 11。

我们把它打印出来。

可以看一下。

你看这里出来了一个 11。

因为我们输出的时候没有换行。

所以直接在后面输出 11。

我们看下一个例子。

在定义变量的时候。

我们也可以一行。

定义很多个变量。

我们整形 x 等于 5。

逗号。

这里用 逗号分隔。

其实就是 int。

就对象当于分号这里。

int y
 等于 6。

再分号。

然后 int z 等于 50。

其实可以写来一行。

用 逗号来分隔。

把三个值都给赋了。

也三个 x y z。

三个变量都定义好。

然后我们求一下它的和。

把它输出出来。

可以看到这里 61。

我们来看常量。

常量就是不变的值。

不变的值。

所以它在定义变量的时候。

前面加一个 const。

所以 const。

就代表这个值是不可变的。

也就是这个 60 是不可变的。

或者说这个浮点整形 。

这个常量 3.14 是不可变的。

我们经常会这样来定义。

像每小时多少分钟。

我们就会定义成一个常量。

我们来看这个例子。

我们把这个买。

num 定义成一个常量以后。

然后我们又对它进行赋值。

可以看到这里已经报错了。

这里有引号可以看到。

它永远都是 15。

它不允许修改。

你看我们编译。

它也是通不过的。

你看这里也报错了。

它不能给赋值一个只读的。

变量

它叫只读的变量。

也就是常量里面。

我们来看为变量构建名称的一般规则。

名称可以包含字母、数字和下划线。

但名称必须以字母和下划线开头，不能以数字开头。

名称是区分大小写的。

你看这小写的买瓦和买瓦是不一样的，是不同的变量。

名称中是不能有空格和特殊字符的。

像井号、百分号这些都不行的。

有一些保留字。

像 C++ 里面关键字，int、stream 这些都不能作为名称来使用。

大家好。

这一课我们来看输入。

首先我们还是引入 iostream 这个输入输出库。

然后这里我们定义了一个整形的 x。

首先我们 Cout 输出一个字符串。

Type aNumber。

然后这里我们用 Cin，两个大于号 x 就表示我们从键盘读入到 x 里面。

注意这里 x 的整形，所以我们只能读入数字。

然后我们用 Cout 输出 yNumber 和 x。

我们来运行一下。

可以看到这里就等着输入。

然后我们输入 5。

出现了。

然后我们看下一个例子。

这个例子是我们先定义了 x 和 y 都是整形，然后我们又定义了一个 Sum 也是整形。

我们先输出 Type aNumber。

然后输入一个字符到 x 里面。

再输出一个敲入一个字符串，敲入另外一个 Number。

再输入一个数字到 
y 里面。

然后是 x 和 y 求和。

求和以后，然后我们输出这和，也就是一个加法计算器。

我们可以看一下。

他先让输入一个 5。

我们再输入一个 2。

好 5 加 2 等于 7。

OK，输入我们就讲到这里。

大家好。

这节课我们来看数据类型。

前面我们也看到了，这个是整形。

int 是整形。

我们把它付给 5，然后我们把它打印出来。

然后这里是浮点型。

float 就是可以表述在小数点的浮点型。

double 就是双精度浮点型，它的精度要比 float 高，就用 double 来表示。

float 和 double 也可以写成科学计数法。

这里带个 e，e 就是 10 的多少次方。

这是 10 的三次方，e4。

大写 E 小写 e 都是可以的，这就代表 10 的四次方。

我们把它打印出来。

x 就是字符型，只能表示一个字符，用单引号把它引起来，这只是一个大写的 D，这个字符，待会我们把它打印出来。

这里 x 也可以写成数字，656667abc。

这里就涉及到另外一个概念。

ASCII 表。

ASCII 表我们可以看一眼。

这个就是 ASCII 表，美国标准信息交换代码。

65。

看这里实际上 65 代表的就是 A，66 代表的就是 B，67 代表的就是大写的 C。

所以这里代表的就是大写的 abc。

其实它字符和数字是共通的。

然后这是布尔型。

布尔型。

我们设两个 ease coding 犯，把它设成 True，或者是把这个设成 False。

好我们运行一下。

我们可以看到，第一个是 5，是吧。

这里输出的是 5。

第二个，浮点型 5.99，双精度的浮点型，我们输出了 9.98。

这个 35e3，也就是 10 的三次幂，也就是 35。

这个 12e4 次幂，也就是 12 万。

这个是字符型，输出是 D，你看这里 abc 都是大写。

这里就是 656667，这是 ASCII 表决定的。

这里输出的 true，true 就是 1。

这里 False 就是 0。

在C++里面都是这样子。

False就是0。

好，我们看下一个。

这里我们再引入一个标准库，叫String。

然后我们可以直接用String来定义一个字符串变量。

我们给它一个值，叫Hello，双引号引起来。


双引号面临的名称是它的值，Hello是它的名称。

然后我们把它打印出来，可以看一下。

可以看到Hello出来了。

好，这期课讲到这里。

大家好，这期课我们来看运算。

我们看第一个。

先把x赋给5，2赋给y。

然后这是加法，x加y。

减法x减y。

乘法是一个星号。

除法是一个杠，余x除以y是多少。

x。

然后这里加加注意，加加在后面意味着先做前面这个事。

Coutx，也就是把x先输出，x因为等于5，就把x输出了，然后加加就是加1，x等于x加1。

那也就是说先输出5，然后x自己再加1，就变成6了。

这是自加，这个加加，你看加加放前面，因为现在下面这句话执行完以后，x等于6，那是先做加加，x先等于x加1，然后变成7了，7以后，然后再输出。

所以它就是输出的是7。

y也是一样，先输出y，y等于2，先把2输出，然后再减减，然后这个时候y等于1。

y等于1以后，然后执行下面这句话，执行下面这句话的时候，先减y，y等于y减1，那也就是说y这个时候等于0，然后再输出y，null是输出0。

好，我们运行一下看一下。

可以看到，第一个x加y，5加2等于7，5减2等于3，5乘2等于10，5除2，这里是整数，记得这是整除，5除2等于2，5除2等于余数是1。

然后x加加，看这里x加加，输出的是5，然后加加x，这里输出的是7。

然后y减减，输出的是2，减减y输出的是0，因为这里y减减以后变成1了，1以后，然后再减减y，所以是0。

好，我们来看第二个例子。

这里赋值运算，x加等3，其实就是x等于x加3，x等于x加3，那这里就是5加3等于8。

x减等3，就是x等于x减3，5减3等于2。

乘等也就是等于x等于x乘3，5乘3，3为15。

除5除3等于1，整除。

下面对一样的。

好，我们运行一下，可以看一下。

你看x加等3等于8，x减等3等于2，乘等3等于15，整除等3等于1，与等3等于2，都是一样的。

后面一货，左进右进都是一样的，与或非都是同的。

好，我看第三个例子。

第三个例子是比较运算符，比较运算符，x是不是等于y，x等于5，y等于2，x是不是等于，这里记住一定是两个等号，两个等号是比较，一个等号是赋值，不等是一个叹号，一个等号代表着不等，大于号、小括号、大于等于、小于等于，他

们返回的都是布尔型。

我们可以看到都是布尔型。

0代表着False。
1确实是x不等于y，所以返回是处。
x确实是大于y，所以返回是处。
x不小于y，所以返回是False。
x大于等于y，返回是处。
x小于等于y，返回是False。

我们来看第四个例子。
这个是与，两个这个符号是与，两个竖线是或，一个叹号就是非。
这个与就是两个都为1的时候，它才为1。
只要有一个为0，它就是一个为False，它整个是为False。
这两个里面，只要有一个为处，它都是处。
只有两个都为False的时候，它才是False。
那这个非就是处，就是False，False就是处。
这个我们看一下。
你看，是吧，零一零。
好，运算符就讲到这里。

大家好，这一刻我们来看字符串。
在字符串的时候，我们要引入一个字符串的库，叫String。
然后我们在定义的时候，要用String，然后输入变量的名，然后给它一个值，字符串的值要用双引号引起来。
我们定义两个变量，一个是FirstName，一个LastName，然后我们又定义了一个String，叫FullName。
FullName，我们两个字符串相连，就直接用加号，就会把两个字符串连起来。
这里就直接将他们两个连起来了。
然后我们将它输出，输出的时候，我们可以看到，他们两个是直接连起来到，中间是没有空格的。
然后我们再看第二个例子。
第二个例子，我们就直接把它加上空格。
三个字符串连起来，FullName加一个空格，再加上一个LastName连起来。
我们把它打印出来。
或者还有一个办法，是用Append。
字符串带有Append的这个方法，直接可以Append后面跟上一个LastName，这个字符串，他们两个也连起来了，和第一个效果是一样的。
我们先看一下，可以看到，你看第一个连接起来了，中间是没有空格的。第二个我们这里加了一个空格，字符串，所以第三个用Append，他们之间也是没有的。
然后我们定义好一个字符串，叫TSC，TSC。
我们想看一下它的长度，它有两个方法，都可以，一个是Last方法，一个是Size方法，这两个都可以看到这个字符串的长度。
我们可以看到这里都是26。
然后我们想读取某个字符串的值，我们这里定一个叫MessDream，这个变量里面是Hello。
它是从0开始，我们直接用中括号加上这个字符，就下标，从0开始，我们就可以读到这个H，可以看到这里就是H。
如果我们想改变的
话，我们直接就把下标直接给它改成J，改成J了以后，它也就变成了J楼。
可以看到这里，字符串讲到这里。

大家好，这期课我们来看算数。
这里我们要引入一个CMess的数学库。
然后我们看它有很多种函数。
第一个Mess函数就比大小，最大值取最小值，5和10谁小。
Squad开平方。
Round45入。
Log自然是数抵达2。
看日子多少。
还有ABS绝是值。
Ack。

Sign, AckCosign, AckTank。

这面临有很多。

Cosign, CosignH。

这面临有很多。

Floor 求他的值。

我们可以看到 PowerX 的 YsMe。

3H, TankH。

我们运行一下。

我们可以看到。

前面。

这个 5 和 10 比大想使 10。

Me，这个是 5。

64 的开平方是 8。

Round 2.63。

Log 2.0.69。

ABS 的 X 的值。

这面临有很多函数。

我们到时候用的时候可以直接用。

好，这些可以讲到这里。

好，我们接着来看条件语句。

条件语句就是这个 if。

if 后面跟一个括号。

括号面临写的是一个 True 或者 False 的表达式。

我们可以看到 20 大于 18。

确实是大于，null是 True。

如果它当为 True 的时候。

那这个大标签面临的名称。

这个大标签面临的名称就会被执行。

这个就是条件。

如果这个条件成立等于 True。

那么大标签面临的就会被执行。

好，我们看下面这个例子。

我们把 Time 设成 20。

如果 Time 小于 18。

那发现这里肯定是不小于 18 的。

那是 False。

False 这一句话就是不会去执行的。

那执行什么呢。

如果 if 这个不执行的话。

那我们看他这里有 else。

那我们就会去执行这个 else。

else 面临这句话。

我们就会打印我的 Uni。

然后我们再看下一个例子。

如果 Time 小于 10。

而知道是 False，不会小于 10。

那它是不会执行的。

那我们还可以再写 else if。

else if 另外一个条件。

Time 小于 25 吗。

20 小于 25 是 True。

这个是成立的。

那我们就打印这个。

如果 else if 执行了的话。


那这个 else 就不会执行了。

这个 Uni 也不会执行。

当然还有一种简单写法。

简单写法我们设一个 Result。

等于一个什么。

等于一个表达式。

这个表达式是先看前面这个。

Time 小于 18 是 True 还是 False。

这里是 False。

False 的话。

那就会执行冒号后面的这个。

把它付给猫。

这个 Uni 就付给这个 Result。

如果它是 True。

null是 Goodday 付给这个 Result。

然后把它打印出来。

好。

我们执行一下看一下。

看到第一个。

因为 20 大于 18。

所以我们就把这句话打印出来了。

然后我们再看这个 20 小于 18 是 False。

所以我们打印的这个 Uni。

20 小于 10 是 False。

20 小于 25 是 True。

所以我们打印的是 Goodday。

打印了 Goodday。

这个 else 就不会执行了。

然后这里 20 小于 18 是 False。

所以 Goodday Uni 付给了 Result。

所以我们把 Result 打印出来。

Goodday Uni。

好。

这几课讲到这里。

大家好。

这几课我们来Ctrl+Switch 语句。

Switch。

这是关键字 Switch。

然后括号。

括号面临这个东西是一定要有一个值的。

我们这里是一个变量。

Date。

我们把它定义成 4。

然后这里下面就是 if 的大括号。

一定要有大括号。

大括号面临名称。

我们先写 case 1。

case 几都可以。

这是它的值。

case 然后冒号。

冒号后面的这两句话。

就是说它要执行的。

我们输出 Monday。

然后 break。

break 是跳出的意思。

也就是说这个 Date。

当它等于 1 的时候。

它就执行这句话。

等于2的时候，执行这个，等于3执行这个，等于4执行这个，这样比 if else 写起来看起来更清晰一些，等于5就执行输出 Friday，等于6。我们可以看一下这个例子。

你可以看到输出的是 Surface。好，我们看下一个例子。

这里多了一个 Default，Default 的意思就是默认。如果这个值，你看 Date 值现在等于4，它
既不符合这个也不符合这个，它就会走到 Default 默认来。我们可以运行一下看一下。你看走到这里了。好，Switch 我们就讲到这里。

大家好，这期课我们来看任务语句。首先我们定一个 i 等于0。这里任务有第一种，是 while 任务，while 后面跟着括号，这里对表单式。当它等于真的时候，我们就会去执行这个大标签面临的名称。因为 i 等于0，i 小于5，它是处于 while 条件，我们就会执行面临。我们把 i 输出出来，然后是 i 进行加1。记得一定要加1，如果不加1的话，那任务那永远都是0小于5，又来0小于5，无限死任务了。那我们左右，我们每次在任务一次的时候，要把这个表达式面临的 i 加1。第一次0小于5，第二次1小于5，2小于5，3小于5，4小于5，到5小于5等于 false 了，5小于5等于 false，那这个它就不执行了。这面临的就不会再执行了，所以它打印出来到是0到4。我们可以先看一下。你看啊，从0打印到4。OK。

然后我们再看第二个例子。我们再把 i 赋0，do while 语句，do while 语句的意思是说，我先不管，我上来先 do，先 do，那就先输出它，先输出它，null是 i 等于0，我直接就输出了，输出一个0，然后这里 i++，i 变成1了。那看1小于5吗HEAD1确实小于5，true，那后来再来执行这个 do，那就输出1，然后加2小于5，然后這樣输出4，2输出3，输出4，4完了加，加4加了以后等于5，5呢HEAD5不小于5了，是 false，那这里就不执行了。注意这里，这里是一定要有个分号的，和这里是不一样的，和这个 while 语句，while 语句你看最后大标签里面对没有分号的。在这里，while 这里是一定要有一个分号存在的。我们可以看到这里输出的也是0到4。可以看到，好，我们后面既续看 for 任务。

我们看第一个例子。for 这里括号，这里有两个分号分开了，三个表达式，第一个代表着 i 是初始值，这个是初始语句，我们把 i 赋成0。然后呢，这个是判断语句，i 是不是小于5，确实是小于5，i 等于0，0小于5，这是判断语句。后面这是自加语句，自加语句的意思就是说这句话执行完了以后，这里再执行这句话，执行这句话，然后再来判断这句话。你看，你说 i 等于0，等于0以后，然后输出这个0，输出这个0以后，然后 i++。

也
就是 i 现在等于 1。

然后判断 1 是不是小于 5，是小于 5。

那继续执行这句话，执行这句话，然后发现输出 1 以后，然后 1 再加，变成 2，2 是不是小于 5，2 小于 5，那执行这句话，然后执行完 i 变成 3，3 是不是小于 5，再输出 3，然后输出 4，这样子。

同样呢，我们还可以这样子来写，你看 i 加加，我们还可以，这个例子，我们可以加 2，我们不加 1 了，我们可以加 2，把这个值赋给 2，也就是 i 等于 0 的时候，0 小于 10，那我们输出 0，输出 0 以后，然后 0 加 2，输给 i，0 加 2，输给 i，i 变成 2 了，2 也是小于 10 的，然后就输出 2，2 了以后，然后这里 2 加 2，等于 4，4 是不是小于等于 10，是小于等于 10 了，那我们再输出 4，那这样子，一次输出，最后输出到 10。

我们看下面这个例子，下面这个例子有一个 break，我们先执行，像上面这个例子，我们可以看到，这里 01234，0246810，这里，这两个例子，01234，这个 024680，好，我们看下面这个例子，下面这个例子，在这里，i 等于 0，i 小于 10，i 加加，这个都是常规的，然后这里判断，如果 i 等于 4 的时候，直接就 break 掉了，这 break 的意思是跳出整个循环，这个循环就不会再继续了，也就是说开始 i 等于 0，i 等于 0，这个不等，输出 0，i 等于 1，这个也不等，等于 i 等于 4 的时候，4 等于 4，4 等于 4 的时候，直接就 break 掉，整个循环就不再执行了，这里4，这句话也不会执行了，然后下面等于 5 也不会执行了，i 等于 5 的时候也不会执行了，我们可以看到这里输出 0123，是吧，到 4 就是不会执行了。

然后我们看 continue，主要看 break、continue 有什么不同，continue 的意思是说，i 等于 4，然后执行这句话 continue，执行 continue 的话，后面这句话就不会执行了，但是下一个循环 i 加加，i 变成 5 了，继续往下执行，也就是单单等于 4，执行到这里，后面的这些话不会执行，不是整个循环跳出，是 continue 后面的这些不会语句不会执行，单一循环的后面语句不会执行了。

我们可以看到这里，你看这里 0123，这里没有
 4，56789。

好，循环我们就讲到这。

大家好，这一刻我们来看数组，数组的话就是在这里，加上一个中括号，里面有一个 4 数值，数值的时候，就是说这是一个 4 个长的字符串数组，这里我们赋值的时候用大括号，然后中间用逗号分隔，里面是字符串，因为这里是定义的是字符串，字符串数组 pass，当然我们也可以定义一个不定长的数组，直接是中括号，这里就不写值了，后面赋值，我们这里赋了 5 个值，那

它就是5个长的，大括号里面用逗号分隔。

当然我们也可以定义整形数组，整形数组我们就是就是int。

这里用中括号，就是写个3，那就是三个长的整形数组。

这里也是大括号，赋值的时候也是大括号，用逗号分隔，有三个值。

在输出的时候，这里我们直接也是中括号，一个下标0，那我们就输出了第一个数组。

它也叫第0个数组，我们是从0开始的。

然后我们对数组进行循环也是一样的，我们i从0开始，i小于4。

那我们输出的时候，我们也可以直接，我们先输出下标i，然后一个冒号、空格，然后我们可以输出cast这个数组，
第0个数组的值，第1个数组值，第2个，第3个。

它是从0开始，一共4个，所以就是0,1,2,3。

我们执行一下，可以看到这里，因为我们这里cast0是WallWall，然后我们循环，第0个WallWall，第1个BMW，第2个福特，第3个马斯达。

好，数组我们就讲到这里，这些课我们来看指针和引用。

我们第1个来看引用，首先我们定义一个字符串，叫Food里面的值是pisa。

然后我们要看这句话，再定义一个字符串，然后这里有一个and符号，and符号跟了一个变量mail，然后指向等于什么呢，给它赋值，赋给了Food，Food里面的值就是pisa。

那也就是说，这里代表说mail的地址，这个and符号就代表着mail的地址，指向了Food的值，也就是指向了pisa。

也就是说pisa对内存里面的一个值，但对内存块的地址是多少呢。

也就是把内存块的地址，mail的地址，它的地址指向了它的地址，指向了pisa这个地址。

也就是这个像什么一样，快捷方式一样，文件里面的快捷方式，也就是它俩这两个变量，现在都指向了pisa内存块的地址。

Food是直接用这个赋值，然后它是把mail的地址指向了Food的这个值。

我们看打印一下，你看我们打印Food的值就是pisa，打
印mail的值也是pisa，说明它们俩指向了统一内存块。

然后再打印这个andFood，打印出来到就是这个Food的这个变量所在的地址，也就是这个pisa这个字符串所在的内存块的地址。

我们执行一下，你看打印出来两个是pisa，这个是这个内存块所在的地址。

这里一定要注意，这就叫引用，引用的意思就是说，我把mail的地址指向了Food的这个变量，也就是说它们俩是指向了统一内存块，這樣就叫引用。

我们看下一个例子，指针。

这里一样，我们先定义一个字符串Food的值叫pisa，然后这里String新ptr这个变量。

或者说也可以这么写，String新ptr也是一样的，都是一样的写法。

ptr这个变量指向了什么呢，这里就好理解了，指向了Food的这个地址。

ptr面临的名称，它这个变量面临的名称是个地址，和前面的不一样，和前面对它的地址指向了这块名称，这两个是不同的概念。

这面临的这个值，ptr面临的值是一个内存地址，就是因为这里有个星，这里有个星，所以它的值是一个地址，地址是什么呢，Food的地址。

然后我们看，把这两个打印出来，把Food打印出来，把Food的地址打印出来，把ptr打印出来。

ptr打印出来，应该就是Food的地址。

然后星ptr，这里星ptr的意思就是这个地址所在的值是啥，就是星ptr这种写法，一定要把星嵌套在前面。

我们可以先运行一下，看一下。你看前四个，第一个Food的pizza，第二个Food所在的地址，你这个ptr的值，ptr的值就是Food的地址。这个然后星ptr就是这个地址所在的这个值，是pizza，看到了，前四个。

然后同事你看下面，我们同样还可以是这个指针所在的这个值，地址所在的这个负值，我们把它负成汉堡包，Hamburger。星ptr我们是可以负值的，它其实和Food是一样的。然后我们把星ptr打印出来，把Food打印出来，我们可以看到两个都是Hamburger。其实他们是指向了统一内存地址，同一块内存名称，然后把它改成Hamburger了，那它也就变成Hamburger，Food也就变成了Hamburger。

好，指针就讲到这里。

大家好，这期课我们来看函数。我们先来看函数。

这里函数也是要有一个类型，这个对返回类型，外的就是空，就不需要返回。看这里int就是整形，所以它就需要返回一个整数。你看这
里Return一个0，然后这里My Function是函数名，然后带着括号，括号面临可以加参数，然后大标签，大标签面临名称就是函数体。可以看到这里Mate，函数名，然后一个括号，然后大标签，大标签面临，这个就是函数的名称，函数体。

可以看到我们这个函数是一个返回值是一个空的函数，面临只是做了一个输出，输出了这么一句话。然后怎么调用呢HEAD因为Mate是主函数，我们从Mate函数进来到时候调用，null是直接写函数名，然后加上括号，加上分号，這樣就会调用到函数，就会执行，执行函数，然后进来就会执行这句话，然后再执行Return。我们可以看一下。你看他输出了这句话。

函数还是比较简then，函数的功能就是把一些相同的功能，把它不用重复写多少遍，我可以调很多遍。我可以看第二个例子。你看第二个例子，这里我们把函数写在了这里，但是Mate调用的时候，如果直接这么调，假如说下面没有函数声明这句话的话，直接调它会爆错，因为它是从上往下的。所以我们要在前面先声明一下函数，声明这函数，就说不需要斜杠实现，不需要写大标签面临的名称，我们只要声明这函数是空的，返回值是空，然后函数的名字，括号加上分号，這樣我们就声明好了一个函数。

這樣我们在Mate调用的时候，我们就可以直接调用。但是它的实现，我们就要在下面来写。同样我们也是Wide，然后买方式和括号，然后这里我们再写大标签面临的名称，這樣这就是它的实现，也叫它的定义，这个叫它的声明。我们运行一下看一下。你看这里也是成功的。

如果我们这里不声明，还是像這樣子，我们只是把Mate写前面，把Mate方式写后面，這樣它会爆错的。我们可以看一下。你看这里就会爆错。

它就找不到函数。

好，我们看第三个例子。

函数，刚才我们说，函数的功能就是这一段话，我们不用写多遍，我们可以用这个某种方式。

我们这里传了一个参数，这个参数的类型是 String 类型的，叫 FName，名字叫 FName。所以我们在调用的时候，那就要把这面临传个字符串进来。你看我们这里调用了三次，调用了三次，那它就会打印三次，这个 Cout 输出三回。所以函数的功能就对象同的功能，我们把它形成一个函数，那就不用写多遍的代码。我们来运行一下，看一下，可以看到这里输出了三个，是吧。

好，我们既续看。

这里我们看这里，我们不光在定义这个变量的时候，我们还写了个等号，等
于 Norway。等于 Norway 的意思，就是给它一个默认值。如果当我们这里不传值的时候，不传值的时候，那这个参数的值就是 Norway。如果这里我们传了值，Sweden，那它这个参数的值就是 Sweden。我们执行一下看一下，你看Sweden, Indian, Norway, USA。这里没传值就是挪威，传值就是它的值。

好，我们看第五个。第五个如果我们有多个变量，怎么办呢就是用逗号分割。我们第一个变量是一个字符串，ifname。第二个变量是个整形，H。然后我们把它输出出来。在传的时候一定要注意，第一个一定是传一个字符串，第二个是一个整形，这是一定要有顺序的。它的定义是什么样子，这里定义对字符串和整形，那这里传值也对字符串和整形，它是一定要有一个顺序的。我们看一下，运行一下，可以看到打印出来了三句话。

好，我们看第六个。第六个这里，我们也可以直接地定义两个，我们这里定义了一个函数，这个函数是传入 X、Y 两个整形，然后把 X 加 Y 的和返回回去。然后这里我们可以直接调用，函数 5 和 3，直接这样写，括号 5 3，这样也是将 5 加 3 计算出来 8，然后输出出来。或者说我们也可以把函数 5 3 作为一个值赋给 Z，Z 也等于 8，把 Z 打出来，我们可以看一下，两个 8。

好，我们看第七个例子。第七个例子，我们可以看到这里有一个 Swap1 和 Swap2，两个唯一的，面临都是一样，把 X 赋给 Z，然后 Y 赋给 X，Z 赋给 Y，相当于做了一个颠倒，中间用一个 Z，把 X 和 Y 做一个互换。但是这里有一点不同，这里声明的时候，这里的 X 是 X 和 Y 都是值，这里是 X 的地址和 Y 的地址。可以看到这两个是引用 X，引用 Y。那我们可以看一下，这两个有什么不同。我们先定义 firstNumber 的 10，secondNumber 的 20。那我们在 Swap 之前，我们打印出来，然后把这两个值打印出来。然后我们在 after 打印出来。然后我们先用 Swap1 做了互换，然后用 Swap2 做了互换，把它俩打印出来。可以看一下，可以看最开始是 10 和 20，是吧，first 是 10，second 是 20，然后 Swap1 做互换的时候，它并没有互换成功，你看 firstNumber 还是 10，secondNumbe
r 还是 20，但是用 Swap2 的时候就互换成功了，是 20 和 10。这里有一个什么问题呢HEAD就是在这里。

antX和antY。

当它传值进来到时候。

用Swap1传进来到时候。

它只是把值传进来了。

X确实等于10。

Y确实等于20。

但是它没有返回值。

X和Y确实也做了交换。

X确实变成了20。

Y确实变成了10。

但是在这里。

它只是把firstNumber赋给了X。

也就是把10赋给了X。

firstNumber和X是指向了两块不同的内存块。

但是它们的值都是10。

Y和second也是一样。

都是指向了不同的两个内存块。

它们的值都是20。

所以X和Y再怎么互换。

外面first和second也不会互换。

但这里是把X的地址指向了first。

Y的地址指向了second。

也就是说它们first和X是指向了同一内存块。

Y和second也指向了同一内存块。

指向的是20。

所以X和Y互换。

也就是这两个内存块会互换。

也就是说first和second这两个值也就会互换。

所以这里是不一样的。

这就是引用。

看到了吧。

引用它因为x的地址指向了first。

所以它们俩指向了同一内存块。

这就是不一样。

我们来看函数的重载。

我们这里有两个一样的函数名。

plus func。

这里也是plus func。

看到但对返回值。

他是int。

他是double。

他的参数也不一样。

他的参数是intX和intY。

这里是doubleX和doubleY。

它面临也不一样。

这个整形的是X加Y。

这个是X加Y。

求它的X。

我们来看这里。

虽然是函数名相同。

但是具有相同函数名。

但是功能是不一样的。

这个就叫重载。

这样就是为了后面方便来写。

他调用的传的值。

你看这里。

plus func传的是8和5。

传的是整形。

也就是说调的是这个函数。

这里传的4.3和6.26。

说明他调的是这个函数。

也重载的意思。

也就是说多个函数名。

多个函数可以具有相同的名字。

但是功能和参数是不一样。

由参数和功能来区分。

它是不同的。

你看我们执行一下。

执行出来到是不一样的。

你看第一个调用的是整形的plus func。

第二个
调用的是double型的plus funk。

这就是函数的重载。

好函数我们就讲到这里。

大家好。

这一刻我们来看C++的类。

什么是OP。

OP就是面向对象编程的意思。

程序化编程。

就指编写程序对数据进行。

操作的程序或者函数。

面向对象编程。

就是同时创建数据和函数的对象。

与程序编程相比。

面向对象编程有几个优点。

第一是更快。

也更容易执行。

第二他的程序结构也比较清晰。

第三个他有助于保持C++代码比较干净。

他不会重复自己。

也更容易维护。

修改和调试。

他也会使用更少的代码。

或者更短的开发时间。

创建完全可以重复的应用程序。

或者可能。

什么是类和对象呢。

类和对象就是面向编程的。

面向对象编程的两个主要方面。

C++是一种面向对象编程的语言。

在C++中的一切都和类对象。

以及他的属性方法相关。

例如在现实生活中。

一辆汽车就可以看成一个对象。

汽车他有属性重量。

颜色以及还有方法。

驾驶。

刹车。

所以属性和方法基本上是属于。

类里面的变量和函数。

这些通常被称为类的成员。

类是对象的模板。

就是说它是抽象的。

对象就是一个实体的真正的汽车。

我们只说汽车这个概念的时候，它就是一个类。

如果说某一辆汽车，它就真的是一个对象。

所以我们可以看这张图，我们 class，类我们可以说是 car，就是真正的一辆汽车。

它可能是 Audi、BMW、Toyota。

所以类是对象的模板，对象是类的一个实例。

描述汽车的时候，描述就是类。

当某个对象被创建的时候，它就会继承这个类中的所有变量和功能。

也就是说，真正有一辆实体汽车的时候，这个汽车它就会继承这个汽车描述中的所有变量，颜色、重量、功能、刹车，还有驾驶这些。

我们来看第一个例子。

这里我们用一个 class 这个关键字来创建这个类。

这个类叫什么HEAD叫 car。

它是分大小写的，大写 CAR。

然后一定要记得用大括号括上。

括号里边的名称就是类的名称。

这里一定不要忘了有分号。

这里是类进行声明、定义。

这里是一定要有分号的。

这里有一个 public，public 是访问关键字，我们在后面来讲。

这里我们定义了三个变量，也叫三个属性。

在类里面的变量，
我们叫做属性。

这里一个 brown 是 string 的，一个 model 也是 string 的，一个 year 是整形的。

这个就是类的定义。

类的定义。

然后我们怎么来声明类的对象呢HEAD

我们创建一个类的对象的时候，跟创建一个变量差不多。

我们用类的名字 CAR，然后后面跟上一个变量名，然后一个分号。

这样我们就创建了一个对象。

有点像创建变量一样，但是类的变量就叫对象，或者叫实例。

这个 CAR object1。

然后我们访问属性的时候，就要用点。

用点就可以访问到对象里面的属性。

类是不能直接调用的。

类大家记得，因为类它只是一段描述，它并没有真正的分配内存。

只有在这里定义实例，或者定义对象的时候，它才真正的分配了一块内存给它。

分配了一块内存给它，那它就是一个空字符串，空的字符串，然后空的一个整形。

这里面没有放东西的。

在这里我们给它赋了一个值，Brown。

这个 Object1 的 Brown赋了一个值。

Object1 的 Model 给它赋了一个值。

Model Object1 的 Year 给它赋了一个值。

这个内存块，这个内存块里面都给它赋好值了。

这新生成了一个内存块。

然后我们再创建一个 2 对象，CarObject2。

这也是新生成了一个内存块。

这个内存块是可以给它进行复制的。

直接复制类是不行的。

类因为现在对一个描述，一个虚的东西，实例实体对象才能给它复制。

我们访问，那就直接可以用 Object1.Brown，就可以访问到了。

CarObject1.Model 也可以直接访问了。

那我们可以直接访问类点它，那是不行的。

因为它只是一段描述，它只是一个描述而已，并没有真正的分配内存。

我们运行一下看一下，可以看到把它都打印出来了，中间有空格分隔。

好，我们来看第二个例子。

第二个例子，我们来看类里面的函数。

你看到这里也叫方法，在类里面的函数叫方法。

看这里我们定义两个函数，一个叫 Speed 的函数，返回是整型，有一个参数是 MaxSpeed。

然后还有一个空函数。

叫MyMatter的。

输出一个HelloWare的这句话。

但是这里这个函数是没有定义的。

你只有定义没有实现。

那我们在下面来写实现。

怎么来写呢。

现
在声明它是int整形。

然后ha这个类名。

两个帽号。

然后斜杠方法名称。

然后这里扩号参数。

然后这里来写实现。

直接返回它的最大。

MaxSpeed的返回。

然后我们来看。

这里先声明一个是象。

叫MyObject。

MyObject。

然后直接输出。

MyObject的函数。

函数也是点。

点Speed的200。

那它这里直接返回。

那应该是输出200。

然后再看这个。

我们再调用MyObject的点。

MyMatter的点。

MyMatter的。

因为它是一个空函数。

Ware的空函数。

但是它执行这句话。

Sealout直接输出HelloWare的。

所以它也会打印出HelloWare的。

我们执行一下。

看一下。

你看这里200。

HelloWare的。

好。

我们来看第三个例子。

第三个例子。

这里有一个跟类名相同的一个函数。

可以看到这里也没有返回值。

也没有什么整形。

intWare的返回值。

这里直接就写卡扩号。

然后这里传了三个函数。

两个Stream。

XY。

一个NTZ。

这个函数就叫构造函数。

因为它和类名相同。

为什么叫构造函数。

就是说在这里创建这个是象的时候。

它这个函数就会被执行。

这个函数就会被执行到。

所以在创建是象的时候。

就必须要传入三个参数。

因为它这里有三个参数。

两个Stream。

一个NT。

所以它叫构造函数。

在创建是象的时候被执行。

它就叫构造函数。

它只要一创建是象。

它就会执行这个函数。

这就是构造函数。

构造函数。

我们来看它我们实现。

也是卡帽号然后卡。

然后我们把它付给了它的属性。

Brund。

X付给Brund。

Y付给Model。

Z付给Yer。

這樣我们在创建它的时候。

传入的是BMWXS1999。

那它的可以看到它的Brund。

null是BMW。

它的Model因为才是Y。

YXS。

那就Model也是Y。

然后Eer就是1999。

因为它在创建的时候。

就给这三个值复职了。

三个属性复职了。

那下面对福特Muston和1969。

我们来执行一下。

你看把它输出打印一下。

可以看到。

可以看到。

好。

好。

我们既续看下一
个例子。

这里你看我们这里intB是没有范围的。

这里Public。

这是有一个Public。

有设了一个X和Y。

这里一个Private设了一个A。

我们来说一下Public和Private。

这就是C++里面类的访问范围。

Public里面的成员像这X和Y。

外部的变量是可以访问到的。

PrivateA或者是B。

如果B不写。

默认的话。

它也是私有范围。

我们来看A和B都是私有范围。

我们看这个。

我们先定义MyClass点MyObject。

MyObject的X等于25。

这个是允许访问的。

因为它是在Public的。

它是公有范围的。

但是MyObject点A赋给50。

但这里它就报了一个错。

它说到它是私有属性。

Private tribute。

因为它A是私有属性。

如果我们这里再写一个MyObject点B，

等于11。

可以看到它也报错了。

它也是一个私有属性。

也是不允许访问的。

所以默认都是Private的。

只有Public是允许访问的。

当然还有一种是Protected。

Protected是继承里面的。

子类可以访问。

所以我们在下面继承会讲到。

我们再看下面这个例子。

我们为了保证它的封闭性，
也就是说敏感，
封闭性就是指敏感的数据，
不想被用户发现，
或者被用户来修改。

像Salary，
一个整形的Salary，
我们就给它设成Private的类型。

外面是访问不到的。

但是如果外面也想用，
也想做修改，
或者说访问的时候怎么办呢HEAD

我们这里设了两个方法。

一个是SetSalary，
一个方法。

我们给一个S，
然后把S付给Salary。

还有一个GetSalary方法。

我们返回Salary的值。

这样我们通过两个公开的方法，
我们就可以访问私有属性的这个值了。

这样做的好处，
主要还是为了保护这个数据。

因为在这个方法里面，
我们不仅仅是赋值，
或者不仅仅对返回，
我们还可以做一些其他的。

假如说我们把它返回成Stream类型，
或者把它是不是零判断一下，
或者怎么样的，
修复啊怎么样的，
我们做一些合法性校验，
经常会在SetSalary或者Get里面做。

所以我们可以看到，
我们先定义这个实例，
Employee，
类名，

然后叫MyObject这个实例。

MyObject点SetSalary。

我们设成5万，
工资是5万。

然后我们输出，
直接用GetSalary来输出。

我们看一下这个例子。

你看这里输出到5万了。

好。

我们继续来看类的继承。

在C++中可以将属性和方法，
从一个类继承到另外一个类，
这就是类的继承的概念。

所以我们就可以有子类和父类的概念。

我们这里定一个WorCo这个类。

WorCo这个类里面有一个Brown的。

我们给它设一个Fold的。

还有一个方法，
Honk输出一个字幕券，
Tutu。

然后我们这里定一个子类，
ClassCard，
然后这里冒号PublicWorCo。

也就是说，
我从这个WorCo来，
父类来继承。

继承到哪呢

继承到在Card里面，
也就是这Card可以有这个属性，
也有这个方法。

同时它还有自己的一个属性，
叫Model。

我们来看把Card创建一个对象，
叫MyCard。

MyCard就可以访问这个，
他父类里面的这个方法Honk，
然后也可以输出，
父类的品牌Bound和他自己的属性Model。

我们来运行一下，
看一下。

这个就是继承。

你看这个都输出出来了。

继承有一个好处，
这样的话，
我可以再进一步的抽象。

细车，
我可以抽象成车辆，
那我这边还可以把它变成一个火车，
对吧

火车来继承它。

细车底下我还可以继承，
某些什么样的SV细车，
轿车这样子。

不断的来抽象，
一层一层的。

我们来看下一个例子。

在继承的时候，
我们这里创建一个父类。

这个父类里面有一个函数叫，
买方式，
他输出一句话。

然后呢，
我再定义另外一个父类，
买Azure，
方式也输出一句话。

那我这一

个子类呢。

这一个子类，class my child class。

这个子类。

那我同时继承两个父类。

这里看清楚。

public my class。

doher public my author class。

所以这里一定是两个 public。

逗号分割的。

继承下来以后呢，当然它里面没有自己的属性和方法。

没关系。

我们就主要是看多继承。

这种就叫多继承。

这个孩子这个类呢，继承了等于是可以继承父亲，也可以继承母亲。

同样继承他们两
个的方法。

然后呢，实现这个对象。

my Object。

那my Object 也可以调这个my方法，也可以调这个my Azure 方法。

我们来看一下。

你看两句话都输出了，this one is pyrenclass and anotherclass。

好。

我们看下一个例子。

这个例子里面呢，我们先看一个基类。

这个基类呢，这里有一个 protected。

protected。

我们上面说，只有子类，这里面的这个变量，是只有子类能访问的。

也就是说你看这里，我们进一个 class program，继承了这个 employee 这个类。

继承了 employee 这个类呢，它呢，在这里面，你看就可以使用这个 salary。

如果这里是 private，私有的，那不好意思，这个 program 也是不能用的。

只能 employee 自己用。

所以你看它这里有两个方法，public 的方法，set salary 和 get salary。

也可以直接是父类里面的 salary 属性，直接进行赋值，或者直接返回操作。

我们可以看一下，先是 program 创建一个对象，my object。

my object 直接调用这个方法，set salary 给设置一个 5 万，然后又给他自己的一个属性 bonus 设了一个 1 万 5。

然后我们把它打印出来，salary 冒号，把这个 get salary 打出来，然后 bonus 把这 bonus 打出来。

可以看到，都打出来了。

好。

类我们就讲到这里。

大家好，这期课我们来看多态性。

多态性的意思，就是多种形式。

它发生在我们许多类通过继承，而得到相互关联的时候。

就像我们上一章规定的那样，继承是让我们从另一个类中，继承了它的属性和方法。

多态性就是使用这些方法，来执行不同的任务。

这样可以使得我们以一个不同的方法，来执行一个单一的操作。

我们举个简单例子，就是说我们这里有一个 animal 的基类。

它下面有一个方法叫 animaelseound。

也就是动物的叫。

我们还可以做一些子类，猪、猫、狗、鸟。

但是他们都有不同的叫声。

名字也叫 animaelseound。

但是它里面的实现，猪是猪的叫声，猫是猫的叫声。

我们看实际例子。

你看我们这里，
首先我们定义了一个 animal 的基类，然后我们实现了一个方法，直接输出一句话。

然后我们定义了一个 pig，来继承 animal。

继承 animal 是同样的，我们这里一模一样的方法，但是这里面的实现名称是不同的。

你看这里输出 the pig says。

然后我们再实现一个 dog，也是继承 animal。

然后这里是 the dog says。

方法也是一样的。

这里我们初始化实例。

有初始化好三个对象。

然后分别调用 animal sound。

我们来看一下。

你看调用出来的都是不同的。

虽然名字相同，但是它其实都是调用自己的。

这就是多态。

大家好。

我们看第18节文件的读写。

在文件读写的时候，我们要引入一个标准库叫 fstream。

一定要引入这个 fstream 来读写文件。

首先我们定一个 ofstream，就是输出。

然后我们先定一个文件，文件名就是 filename.txt。

给它一个 myfile 对象。

我们创建一个文件，这是一个空文件，用 ofstream 来创建。

创建了以后，我们就用大标签像 cout 一样输出。

把它就输出，这句话就输出的 myfile 里面去了。

最后一定要记得是这个文件进行关闭。

你看我们执行一下。

你看这里就执行成功了。

我们可以看的，这里就有一个这个文件。

你看这里这句话，写的这个文件里面了。

好。

我们来看文件的读写。

文件读写同样是引入 fstream 标准库。

引入来以后，我们先定一个字符串。

这里我们要用 ifstream，我们因为要读取这个文件，就是 in ifstream。

然后我们定一个变量叫 myfile。

然后同样读取这个 txt 文件。

然后读的时候，我们用 getline 这个函数。

getline 这个函数，首先先传入文件对象，然后把它读的哪个 stream 里面去。

它是一行一行读。

然后我们用 cout 把它输出出来。

最后也要记得文件是一定要关闭的。

我们运行一下看一下。

OK。

成功了。

我们看第19节异常。

程序员在写程序的时候，会有一些程序编码错误。

或者说在网络请求的时候有possibly超时，或者在访问文件的时候，有possibly文件不存在。

所以它会抛出一些异常。


我们就要捕捉这种异常来进行处理。

因为它是不可控的，有possibly这种错误那种错误。

所以我们就需要使用 try 和 catch 这种模式。

try 里面我就要写，假如说我读取某个文件，或者我写文件。

写文件的时候磁盘满了，对吧HEAD

或者请求某个网络响应超时了。

那我都在 try 里面来写有possibly发生的异常。

就在 try 里面来写，然后如果发生了异常以后怎么处理，我们就在 catch 这里面来写。

那我们看这个简then例子。

这个简then例子是说，我们定一个 a 值等于 15。

如果它大于 18 的话，那它就应该是输出一句话。

如果不大于 18，那我们就要抛出一个异常。

throw。

例子一般来说，这里面不会有throw的。

某个函数里面才会有throw。

然后我调网络函数调请求的时候，那里面possibly超时了，throw出去。

或者说不存在了，我把它throw出去。

然后我们例子里面，我们就throw一个整形出来。

在 catch 的时候，因为它这里是个整形，所以我们 catch int。

然后给一个变量，到时候throw出来到变量的值就会放到这里面。

然后我们就输出这两句话。

我们可以看一下这个例子。

你看这里输出了 a 值等于 15。

好。

我们看下面这个例子。

下面这个例子同样也是throw 505，但是这里 catch 不一样。

开始是三个点，三个点的意思是说，那我就要把所有异常都捕获出来。

我不管它是整形的异常，或者是其他类型的异常，我都要捕获出来。

你看这里，它就直接也输出了这句话，就是。

所有异常捕获。

就是三个点。

好。

这一句话讲到这里。
