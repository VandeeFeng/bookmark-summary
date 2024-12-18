Title: 欢迎来到 HDR 照片时代：增益图 HDR 与 HDR 工作流 - 少数派

URL Source: https://sspai.com/post/94425

Published Time: 2024-12-18T07:00:00.000Z

Markdown Content:
欢迎来到 HDR 照片时代：增益图 HDR 与 HDR 工作流

HDR 视频大家都很熟悉了，因为视频，特别是电影，引入 HDR 技术的商业价值更高。iPhone 能拍摄**杜比视界**的视频，而其他品牌手机能拍摄 **HDR10** 兼容的视频。直播一般使用的是 **HLG HDR** 视频。这些都是成熟、且在各自领域已被被广泛兼容的标准。

然而照片并没有这么好的待遇，直到 2023 年 Adobe 和 Apple 才联合发布了第一版 HDR 照片标准 ([ISO/TS 22028-5:2023](https://www.iso.org/standard/81863.html))，在后文中这一标准称为 **ISO HDR**。

HDR 与 SDR 的区别
-------------

ISO HDR的标准实际上照抄了影视行业的做法。HDR 的全称是高动态范围 (High Dynamic Range)，也就是说图像中暗部和亮部细节都要完好保留。一张图来解释之：

![Image 46](https://cdnfile.sspai.com/2024/12/01/036d5959aea6452bdb30f49a93daa50a.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

对 HDR 与 SDR 的直观解释。素材 ©Mircea Iancu on Pixabay

在 SDR 屏幕上直接不做处理查看 HDR 照片，看到的效果如上图的左 1。本文使用张家界天门山的一张照片作为演示，左1的实际效果如下：

![Image 47](https://cdnfile.sspai.com/2024/12/01/05dc5d85511a1610d9ce5beae09a56a0.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

不经过处理查看HDR的效果和照片过曝一致

该如何解决？方法被称为色调映射 (tone mapping)，也就是将 HDR 信息压缩进 SDR 的高度，有很多种不同的方案，得到的结果也不同。类似于左 2 的压缩方式效果为：

![Image 48](https://cdnfile.sspai.com/2024/12/01/327c24023937b624e8a62e710b177de7.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

看起来正常很多了的SDR照片

那真正的 HDR 照片是什么样子的？我也附了一张在下方。但你看到它的时候已经不是 HDR 了，因为有三个阶段可能出现问题：

![Image 49](https://cdnfile.sspai.com/2024/12/01/8664654a5a4114a3309a2edaeef32f20.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

真正的 HDR 照片，但它已经被服务器转换了，所以你看不出来

*   **服务器端的压缩**：一张照片上传到网上，服务端可能会为了节约空间将其压缩为其他格式以减少体积，在这个过程中可能会丢失 HDR 信息，属于传输问题；
*   **设备对 HDR 内容进行解码**：要求设备能将该照片识别为 HDR，例如对于浏览器：桌面版的 Chrome 和 Edge 支持显示增益图 HDR，但 Safari 全系不支持。Windows 11 的图库对 HDR 有限支持，而 Apple 平台在 iOS/iPad OS 18.1 以及 macOS 15.1之后，基本支持主流的 HDR 格式。此外，App 客户端需要额外参数才能实现 HDR 显示。这些属于软件问题；
*   **兼容的显示器**：要求设备屏幕支持 HDR 。属于硬件问题。

我们暂且不考虑问题 1 ，而问题 3 是钱就能解决的（买新硬件）。问题 2 是普及 HDR 照片的关键。

回到 ISO HDR 上来，我们知道，每个像素点可用四个整型 (Int) 来表示，即 R、G、B 以及透明度 A。为方便其见，我们只考虑一个通道（即只考虑 R）。在 8 bit 下的照片中，最亮的亮度记为 255 (2^8−1)，而最暗的像素记为 0。

![Image 50](https://cdnfile.sspai.com/2024/12/01/2ceadbef5bf87f21689a09427774002a.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

从0到255的灰度图

我们把 255 对应的亮度记为 SDR 下的最大亮度，其标准为 200 nit。超过 200 nit 的部分就属于 HDR 的范畴了：

![Image 51](https://cdnfile.sspai.com/2024/12/01/af5700d08e1192d71fd2c76a89cbdf65.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

超过 200 nit 就进入到 HDR 的范围（此图片已转化为 SDR）

最简单的处理办法，就是声明该图片是 HDR 的。超过 SDR 范围的像素用大于 255 的数值去储存之。照片的位数也需要从 8 bit 增加到至少 10 bit。在 10 bit 下，亮度最大为 1023，相当于是 255 的  3.11 倍。

为什么不是 4 倍而是 3.11 倍？这涉及到伽马这个参数。简单来说就是人的眼睛对光的感受是对数的不是线性的。如果四个图像看起来的亮度依次为 1、2、3、4，那实际光强为10:43:106:200。一般来说显示器的伽马为 2.2，4^(1/2.2) = 3.11。

所以继续沿用 2.2 的伽马，10 bit 并不够用！对于一个亮度最高 6400 nit 的物体（相当于 SDR 的 32 倍），我们需要 8+14 = 22 bit 才能储存，这一开销（接近 3 倍的文件体积）是不合算的。PQ 和 HLG HDR 定义了一个映射方式，对高亮度数据占用的信息进行压缩。因为人眼对光的敏感性是指数的，比如说只有亮度差大于 2% 才能肉眼看出来。因此记录数据时，没必要从亮度 500 至 600 每隔 1 就记录一下，完全可以 500、510、520、531、541、552…… 大幅减少所需的数据量。选择合适的映射方式，使用 10 bit 就能在不丢失肉眼精度的情况下，将数据映射到最高 10,000 nit 的亮度。

![Image 52](https://cdnfile.sspai.com/2024/12/01/082157b125fc0a450a3ac74e7e66335c.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

伽马 2.2 的曲线（红）与某种 HLG 的曲线（蓝色）

我们把整型映射到 0-1 范围的浮点中。在 SDR 空间中，200 nit 的亮度以 1.00 储存。而在上图对应的 HLG 中，这一亮度大约以 0.55 进行储存。1000 nit 的亮度将以约 0.75 进行储存（横坐标 5），而 1.00 的数据会对应 2400 nit 的亮度。我们把这个照片最高支持的余量 (headroom) 称为 12，即表示 HDR 亮度最大为 SDR 的 12 倍。

现在来考虑该如何解码这一图像。如果软件知道你使用的是 PQ 或者 HLG ，那它将正确的把 0.55 映射到 200 nit、0.75 映射到 1000 nit、1.00 映射到 2400 nit。但如果软件并不知道，仍然以错误的伽马 2.2 对其进行处理，那么这些亮度将变成 110、150 以及 200nit，即出现了色调映射（好在 HLG HDR 考虑了这一问题，这种映射不能说是错误的，因为 SDR 部分得到了正确呈现，只不过亮度有所降低）：

![Image 53](https://cdnfile.sspai.com/2024/12/01/df76b3e8da9ed945326c0ed4fe5b3de7.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

这是一个以 HLG 曲线储存的照片，如果你用浏览器查看能看到 HDR 效果

第二个问题在于，创作者可能使用的是最高 1600 nit 的显示器，并创作了在这个范围内的作品，但观众使用的是最高 400 nit 的显示器，其只能显示比 SDR 亮一倍的内容。这个时候，有两种办法进行处理。第一个称为滚降 (roll-off)，第二个被称为硬切 (hard-clipping)。

![Image 54](https://cdnfile.sspai.com/2024/12/01/a1aca59d410d9b90cf9d855d4e4f0c46.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

滚降和硬切的解释

滚降本质上也是一种色调映射，且这种操作是软件（甚至是显示器本身）进行的，不可控。那有没有办法做到最大的兼容性？最简单的做法就是：我把 SDR 和 HDR 照片打包一块，支持你就看 HDR，不支持就 SDR。

这一方法最大的缺点就是——文件体积翻倍。有没有优雅一些的方案？这时候增益图 HDR 就出来了。

增益图HDR
------

早在 2020 年，Apple 发布 iPhone 12 后，就引入了私有的一套 HDR 储存、显示流程，被称为 Apple HDR。简单来说，我们只记录 SDR 图片本身（称为基本图），以及 SDR 与 HDR 之间的亮度差异作为增益图：

![Image 55](https://cdnfile.sspai.com/2024/12/01/575c6eb985a835b0d73e52e28ed54bed.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

增益图 HDR 的图示 ©Google

上图左侧为 HDR 照片，中间为 SDR 照片。两个照片的亮度差异可用单色的右图表示。单色照片储存所需的空间要小得多，因此整体文件大小不会比 SDR 多多少。

![Image 56](https://cdnfile.sspai.com/2024/12/01/fcfd65085b49742a36180305077f3e77.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

天门山照片的增益图，其信息量很少因此占用空间不多

Apple HDR 是私有的，后来 Adobe 申请了一系列专利，并拉上 Apple 一块推出了增益图 HDR 的国际标准 ([ISO/DIS 21496-1](https://www.iso.org/standard/86775.html))，在本文中称之为 **ISO 增益图**。

在 ISO 增益图标准中，增益图通道数量可选单色或者 RGB。RGB 增益图包含三个通道，其体积也相应地会有增加。比如 iOS 18 开始，iPhone 15、16 系列拍摄得到的是 RGB 增益图的 HEIC 或 JPG，iPhone 14 及之前得到的是单色增益图的 HEIC 或 JPG。

![Image 57](https://cdnfile.sspai.com/2024/12/01/e9136430246583c2c4ccb19585a09102.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

通过上变换获得 Adaptive HDR（Apple 平台的 ISO 增益图 HDR）©Apple

增益图每个通道的每个像素，取值范围会映射到 \[−1, 1\]。正数表示在基本图的基础上增加亮度，负数表示在基本图的基础上降低亮度。因此 ISO 增益图，可以用 HDR 照片作为基本图，SDR 照片通过 HDR 和增益图计算出来。

ISO 增益图 HDR 支持的格式包括：JPEG、HEIC、AVIF、JXL、TIFF 等。理论上每个格式都有单色和 RGB 增益图两个选项。HEIC、AVIF、JXL、TIFF 等格式可选下变换（HDR 作为基本图）或者上变换（SDR 作为基本图），下变换还可以选择 PQ 或者 HLG 作为 HDR 基本图的曲线。粗略来看，一共有**超过 34 种可能的组合**。

又回到兼容性上来，毕竟 ISO 增益图是 2024 年才推出的标准，并不是所有的组合在目前都能被广泛兼容。

谷歌负责 JPG 格式的增益图的实际应用，并制定了 UltraHDR 库（即 JPG 格式的增益图 HDR）。UltraHDR 有两种可能的方式：单色增益图或 RGB 增益图。即使 UltraHDR 种类只有两种，但兼容性也存在问题。

![Image 58](https://cdnfile.sspai.com/2024/12/02/ec27455f2928a92ce84b05c6941673c9.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

UltraHDR 的文件结构 ©Google

例如在 iOS 18.1之前，Apple 设备（macOS 除外）无法识别 Adobe 输出的 RGB 增益图 JPG 文件。现在支持分享 HDR 图片的社区（例如 Instagram、酷安），也都会先把任何格式的 HDR 转化为单色增益图 JPG，并可能导致亮度的一些变化。

所以，并不建议直接分享 ISO HDR 或者 RGB 增益图 HDR，而是需要将他们转化为单色增益图 HDR。在考虑这个问题之前，我先总结了获得 ISO 增益图 HDR 的方法：

*   **Android 手机直接拍摄**：获得的是单色增益图的 UltraHDR，UltraHDR 在 Android 14 引入；
*   **Adobe 的 ACR 输出**：获得 RGB 增益图的 JPG、TIFF、PNG、AVIF 和 JXL。其中 JPG、AVIF 和 TIFF是上变换，JXL 是下变换；
*   **iPhone 拍摄**：15 和 16 获得 RGB 增益图的 HEIC 或 JPG，14 以及之前获得单色增益图的 HEIC 或 JPG；
*   **使用 libultrahdr 库**：可输出单色或 RGB 增益图的 JPG；
*   **使用 Apple 平台的 ciimage api**：可输出 RGB 增益图的 HEIC 或 JPG。

HDR照片工作流
--------

### 软件：

桌面端，处理 RAW 文件首选使用 Lightroom（收费），Darktable （开源软件）支持输出EXR、AVIF (PQ HDR) 格式的照片，Photomator（收费）支持输出 ISO HDR 文件。

移动端仍然建议使用 Lightroom（收费）。Photomator（收费）等软件也支持输出 ISO HDR 文件。

### 显示器：

桌面端你需要一个 **HDR1000 认证**的显示器获得最佳效果，最低也要 HDR600。推荐使用 m1 pro 芯片以后的 14 或 16 寸MacBook pro，最高支持 1600 nit 亮度。其余 MacBook 在中低亮度下可提供最高 1 档的余量 (headroom = 2)。

![Image 59](https://cdnfile.sspai.com/2024/12/01/43a2c6bc260cf5428a4981676a88c3a8.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

HDR1000 的显示器在保证 SDR 200nit 的情况下还有 2 档以上的 HDR 空间

移动端建议 iPhone12+（不包括 SE3）或 Android 14+ 系统且支持 HDR 显示的安卓。iPad 只建议最新的 m4 pro 或者 miniLED 款 12.9寸 pro，否则只能提供最高 1 档的余量：

![Image 60](https://cdnfile.sspai.com/2024/12/01/article/d58b28d97ce83aeb9414545cd5f1f122.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

Apple 设备的 HDR 兼容性，最高 5x SDR 才有较好效果 ©Apple

### 输出与储存

处理完成后，照片以 HDR 的格式进行输出，LR 可直接输出 AVIF、JPG 或 JXL 等小体积格式。或者输出 16 bit 的 ISO HDR（如 PNG、TIFF）、EXR 作为中间文件进行后续压缩。

![Image 61](https://cdnfile.sspai.com/2024/12/02/8bd6810864c620d370d3ba9236ed181f.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

目前 LR 支持输出 5 种 HDR 格式

根据需求，对照片进行压缩。如果不需要兼容性（例如只储存在本地，不分享不上云），可采用 ISO HDR 进行储存。建议使用 10bit HEIC、AVIF 或 JXL，曲线可选 PQ 或 HLG。

如果需要兼容性，例如社交软件分享，云储存，可选单色增益图 HDR，或者使用 RGB 增益图 HDR，等未来普及（比如目前 Google Photos 不支持识别 RGB 增益图 HEIC）。

不推荐以 UltraHDR 储存，JPEG 压缩效率低质量相比较差。但可以将其用于照片分发。

![Image 62](https://cdnfile.sspai.com/2024/12/01/dba2ce73b5a7a9fe6fb3a4bf6b97cca7.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

macOS平台生成HEIC HDR的CLi工具

在 macOS 平台，我写了一个命令行工具用于将 HDR 照片转化为 ISO 增益图或 ISO HDR 格式的 HEIC 文件。支持生成单色增益图获得最大兼容性。软件以 MIT 协议开源。

\> 关注 [少数派小红书](https://www.xiaohongshu.com/user/profile/63f5d65d000000001001d8d4)，感受精彩数字生活 🍃

\> 实用、好用的 [正版软件](https://sspai.com/mall)，少数派为你呈现 🚀

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。
