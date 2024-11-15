---
title: the equation of cat motion
date: 2024-11-15
extra:
  source: https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of
  original_title: the equation of cat motion
---
## Summary
**摘要**：
本文采用经典力学的视角，通过一个方程来理解和模拟猫面对人类时的行为。该猫被视为受由人类施加的力场作用的质点。本文提出的方程能够重现猫的多种典型行为模式。文章探讨了猫行为中的一些特征，如它们对呼唤无应的偏好、长时间停留在偏爱者身边、进行随意的“zoomies”等活动，甚至身体质量较大的猫也表现出仿佛能够“漂浮”的特殊行为。此外，文章通过引入时间随机的外力项，模拟猫的随机行为和它们的喘息声。

**要点总结**：
1. **猫的行为**：本文以猫为研究对象，从经典力学的角度，借助一个模型为基础方程，重现了猫在人类面前表现出的七种行为模式，包括偏好保持一定距离的行为、产生飞虫干扰时会离开某个位置等。
2. **物理模型的构建**：猫被建模为质点，并通过外力场研究他们的行为。模型考虑了外部刺激与潜在态的相互作用，解释了猫的行为模式。
3. **现象的物理说明**：本文通过引入时间随机的外力项来说明猫的随机行为，以及通过周期外力来解释猫的喘息声，这些都是经典的物理现象在猫行为中的应用。
4. **学科交叉应用**：本文结合猫的行为学与物理学，探讨了猫的行为特性如何借助物理学原理进行简洁的解释，同时也为教学提供了有趣的例子。
5. **教学价值与研究前景**：物理模型的建立不仅为教学提供了可视的、易于理解的例子，还激发了对猫行为研究的新思路，深化了我们对这些迷人生物的理解。这样的一种跨学科研究方法可以拓宽学生的科学视野，增强对经典力学概念的理解和兴趣。
## Full Content
Title: On cat–human interaction from the viewpoint of physics: An equation of motion

URL Source: https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of

Published Time: 2024-11-01

Markdown Content:
[Skip Nav Destination](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#)

PAPERS| November 01 2024

Anxo Biasi

Laboratoire de Physique de l'Ecole Normale Supérieure ENS Université PSL, CNRS, Sorbonne Université, Université de Paris

, F-75005 Paris,

France

Search for other works by this author on:

![Image 1: Crossmark: Check for Updates](https://crossmark-cdn.crossref.org/widget/v2.0/logos/CROSSMARK_Color_horizontal.svg)

_Am. J. Phys._ 92, 827–833 (2024)

*   [![Image 2: American Association of Physics Teachers](https://aipp.silverchair-cdn.com/data/SiteBuilderAssetsOriginals/Live/Images/aapt/logo.png)](https://pubs.aip.org/aapt)
    
     [![Image 3: American Journal of Physics](https://aipp.silverchair-cdn.com/data/SiteBuilderAssets/Live/Images/ajp/aapt-americanjournalofphysics-vr2-815595398.svg)](https://pubs.aip.org/aapt/ajp)
    
*   [Split-Screen](https://pubs.aip.org/aapt/ajp/article-split/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of)
*   _Views Icon_ Views
    *   Article contents
    *   Figures & tables
    *   Video
    *   Audio
    *   Supplementary Data
    *   Peer Review
*   [Open the PDF for in another window](https://pubs.aip.org/aapt/ajp/article-pdf/92/11/827/20213524/827_1_5.0158200.pdf)
*   _Tools Icon_ Tools
    
*   Search Site

This paper provides an enjoyable example through which several concepts of classical mechanics can be understood. We introduce an equation that models the motion of a cat in the presence of a person. The cat is considered as a point particle moving in a potential induced by the person. We demonstrate that this approach to the problem reproduces characteristic behaviors of these curious animals. For instance, the fact that cats do not typically come when they are called, or that they remain longer on the lap of their favorite person; even “zoomies” are reproduced (cats randomly run back and forth across the house). We use this model problem to explore topics of current research such as stochastic equations and periodically driven systems. The pedagogical value of this work and its potential use in teaching are discussed.

I. INTRODUCTION
---------------

Cats are such charming animals that people frequently immortalize them in pictures and videos that are shared with friends, relatives, or even the world. The popularity of cats has grown to the point that they gained their own spot on the Internet, occupying a significant portion of the content on social media. A quick search reveals numerous cat accounts that have amassed millions of views and followers. This astonishing popularity is partly due to their unique behavior. But what causes these animals to behave in their characteristic way? This paper offers a physical perspective on the subject. In the low-energy limit, when cats are calmer, we have identified seven common behaviors of cats and built an equation that qualitatively reproduces them. To our knowledge, this work is the first to model features of cat behavior with an equation, although other cat features have already been explored by physicists, such as their incredible ability to land on their feet.1–3

We will model the cat as a point particle and see what energy potentials can explain the collection of behaviors cats display in the presence of a person, which we list in Sec. [II](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#s2). In Sec. [III](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#s3), the model equation of cat motion is introduced, and in Sec. [IV](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#s4), we explore how potential minima and friction combine to reproduce some of the characteristic behaviors cats display. In Sec. [V](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#s5), the stochastic version of the equation of motion is introduced to show that a random forcing term can be added to reproduce random behaviors of cats. In Sec. [VI](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#s6), purring is explained in our model by the presence of an external periodic forcing term that improves the stability of equilibrium points.

This work combines classical mechanics with an intriguing story that may be used to familiarize students with concepts like equilibrium points, potential barriers, friction, or external forcing. These concepts may be, of course, introduced just by using traditional point particle setups. However, it is common that students in initial courses find difficulties in the abstract nature of physics.4 In particular, unfamiliar setups (e.g., a system of particles) hinder the visualization of key ideas. This paper's approach may help students better understand mechanics concepts thanks to three elements: (1) the low level of abstraction demanded by our setup (a cat and a person), (2) the ease of visualization of this real world scenario, and (3) the curiosity aroused in both expert and general audiences. For these reasons, we believe this work may turn into valuable material in introductory classical mechanics courses.

II. CAT BEHAVIOR
----------------

The inspiration to understand cat behavior from the viewpoint of physics came from our cat. Since she arrived, we started to observe peculiar behaviors in her interaction with us. After some time, we noticed repetitive patterns, making us view her motions as those of a point particle (a physicist never rests!). We realized that her dynamics are rather simple, with well-established equilibrium points that are stable or unstable under external stimulus. Then, we started thinking about whether some of her characteristic behaviors could be modeled by an equation. We here focus on a simple scenario of the cat–human interaction: _a single cat in the presence of a single person at rest_. The dynamics we observed are the following:

*   **P1:** Cats commonly rest keeping some distance from people.
    
*   **P2:** When cats rest on a person (e.g., on the lap, belly, back), minimal stimuli may provoke them to leave that position (e.g., a fly, an imperceptible sound, a _β_\-decay of an atom in a neighboring galaxy). The intensity of perturbations needed to produce the departure depends on the attachment cats have to the person they are resting on.
    
*   **P3:** When cats are petted by people, they move back and forth in an oscillatory motion.
    
*   **P4:** When cats are called by people, they seldom respond.
    
*   **P5:** When cats decide to approach the person who calls them, they often get distracted on the way and do not reach the person.
    
*   **P6:** At night, cats randomly run back and forth across the house. These episodes are called “zoomies” (and we invite the reader to search for some videos on the Internet!).
    
*   **P7:** Cats purr (emit a soft and vibrating sound) when they like being petted by a person.
    

Points **P1–P7** have been extracted from the observation of the quotidian life of our cat, discussions with friends about their own cats, the common lore, the lore on the Internet, and specialized material on cat behavior.5,6 Therefore, they are not universal and some cats may display a weaker version of some of them. Note that this is a theoretical work intended for physics education and that no experiments on animals have been conducted.

III. THE CAT'S EQUATION
-----------------------

Our working hypothesis is that cats behave as if they perceive a force around a person. As a first approximation, we consider that their dynamics are modeled as a point particle obeying Newton's mechanics in the presence of an external potential Vcat(δ) (induced by a person at rest) and a friction term,

md2xdt2\=−dVcat(δ)(x)dx−ϵdxdt,

(1)

where x(t)∈ℝ represents the cat's position at time _t_ with respect to the person placed at _x_ = 0, _m_ \> 0 is the cat's mass, and ϵ\>0 is the friction coefficient with values that depend on each cat. In the Sec. [IV](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#s4), we will see that the following potential reproduces behaviors **P1**–**P5**, giving a good idea of how cats perceive the presence of people (see Fig. 1):

Vcat(δ)(x)\=g(x2−1)x2x2−δx2+δ.

(2)

This form is based on a rational function for the control it provides over the equilibrium points, enabling us to manage their number, relative position, and stability. As we shall see, these are the key ingredients, together with friction, to reproduce behaviors **P1**–**P5**. _g_ \> 0 is the coupling constant (set to _g_ = 1 from now on to simplify the notation, but this does not alter the qualitative picture of the model), and δ∈\[0,1\] reflects the attachment the cat has to the person. For _δ_ = 0, the point _x_ = 0 (the person's position) is unstable: the cat has no attachment to the person. On the other hand, for δ\>0 the point _x_ = 0 is stable, as Fig. 1 shows. Larger values of _δ_ are associated with stronger bonds. For _δ_ = 1, the minimum at the origin is as deep as the off-centered ones, indicating that the cat has a very strong attachment to the (lucky!) person.

Fig. 1.

![Image 4: Interpretation of the cat–human interaction potential  Vcat(δ). In (a), the cat is attached to the person ( δ=0.14), while in (b) the person is a complete stranger to the cat (δ = 0). In both cases, the cat is illustrated at rest at three equilibrium points of  Vcat(δ).](https://aipp.silverchair-cdn.com/aipp/content_public/journal/ajp/92/11/10.1119_5.0158200/1/m_827_1_5.0158200.figures.online.f1.jpeg?Expires=1734672380&Signature=eFPInFxbUEzPV4f3rp5n~vcGCcztm-atGRMTNAcbj4UmZta1EZ-vB757nrB14MDf~wYdFB7czuPb5nsn75-A8mM8gt65hdnqLzFld18ZDU272C5oHKFXNncWyh60BjERIhLzcez51YKs~GczCqnmVldPw~neCzc~9jqezik-iTIgcXHAIlgsSfjuzJTiS2GAdEL5Q1yXsipSCR~EC~HZRy6Lgj3SfR8rsNoD3xpZzM396GL30pCE7Doue2hxujBHlR9oWF5pc76aqsriUy2uF1LIBQQzYpFNfQySNMf1qdV73d6P3DRbzGzLZLWIlqfmpN9QYV1LJ-uWLefai7D0hg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Interpretation of the cat–human interaction potential Vcat(δ)⁠. In (a), the cat is attached to the person (⁠ δ\=0.14⁠), while in (b) the person is a complete stranger to the cat (_δ_ = 0). In both cases, the cat is illustrated at rest at three equilibrium points of Vcat(δ)⁠.

Fig. 1.

![Image 5: Interpretation of the cat–human interaction potential  Vcat(δ). In (a), the cat is attached to the person ( δ=0.14), while in (b) the person is a complete stranger to the cat (δ = 0). In both cases, the cat is illustrated at rest at three equilibrium points of  Vcat(δ).](https://aipp.silverchair-cdn.com/aipp/content_public/journal/ajp/92/11/10.1119_5.0158200/1/m_827_1_5.0158200.figures.online.f1.jpeg?Expires=1734672380&Signature=eFPInFxbUEzPV4f3rp5n~vcGCcztm-atGRMTNAcbj4UmZta1EZ-vB757nrB14MDf~wYdFB7czuPb5nsn75-A8mM8gt65hdnqLzFld18ZDU272C5oHKFXNncWyh60BjERIhLzcez51YKs~GczCqnmVldPw~neCzc~9jqezik-iTIgcXHAIlgsSfjuzJTiS2GAdEL5Q1yXsipSCR~EC~HZRy6Lgj3SfR8rsNoD3xpZzM396GL30pCE7Doue2hxujBHlR9oWF5pc76aqsriUy2uF1LIBQQzYpFNfQySNMf1qdV73d6P3DRbzGzLZLWIlqfmpN9QYV1LJ-uWLefai7D0hg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Interpretation of the cat–human interaction potential Vcat(δ)⁠. In (a), the cat is attached to the person (⁠ δ\=0.14⁠), while in (b) the person is a complete stranger to the cat (_δ_ = 0). In both cases, the cat is illustrated at rest at three equilibrium points of Vcat(δ)⁠.

Close modal

The asymptotic growth of the potential, Vcat(δ)(x→±∞)→∞⁠, is used to keep the cat close to the person, modeling that cat and person are confined in the same room. Potentials with this kind of asymptotic growth are often encountered in research, as experiments in a laboratory are usually localized in space. For instance, they are used in cold atom experiments,7 or for modeling light propagation in some optical fibers.8

The friction term in Eq. (1) is needed to reduce the energy,

E\=m2(dxdt)2+Vcat(δ)(x), dEdt\=−ϵ(dxdt)2,

(3)

otherwise, the cat does not converge to resting positions after periods of activity. Note that, in order to oppose the cat's motion, we need ϵ≥0 and friction must be proportional to an odd power of the velocity. Finally, let us note that the cat moves in a three-dimensional space. However, since the most important parameter is the distance between the cat and the person, we assume the cat moves along a line, which further simplifies the analysis.

IV. REPRODUCING CAT BEHAVIORS P1–P5
-----------------------------------

In this section, we show that the cat's equation (Eq. (1)) captures qualitatively the phenomenological observations **P1**–**P5**.

**P1**: “_Cats commonly rest keeping some distance from people_.” This behavior is captured by the off-centered global minima present in Vcat(δ)⁠, as illustrated in Fig. 1. The cat may start at many positions with different velocities but will end up at the minima due to the friction term. On most occasions, the final position will be a global minimum, specially for a weak bond between the cat and the person (small _δ_). However, if the bond is strong enough, the person's position competes with the off-centered minima for the cat's preference to rest. This scenario is captured by our model when δ→1⁠, as _x_ = 0 becomes an additional global minimum.

**P2**: “_When cats rest on a person (…), minimal stimuli may provoke them to leave that position (…). The intensity of perturbations needed to produce the departure depends on the attachment cats have to the person they are resting on_.” The first part of this statement is reproduced by the equilibrium point of the potential at _x_ = 0 (the person's position) because the cat may rest on the person x(t)\=ẋ(t)\=0⁠. The second part of the statement is captured by the dependence of the potential on _δ_. From the second derivative at the origin,

d2Vcat(δ)dx2|x\=0\={−2if δ\=0,2if δ\>0,

(4)

we see that _x_ = 0 is unstable for _δ_  = 0, indicating a departure of the cat from the person under arbitrarily small perturbations. On the other hand, for δ\>0⁠, this position is stable and stronger stimulus is needed to detach the cat from the person as _δ_ grows. In Sec. [VI](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#s6), we will see that other phenomena have stability regions that depend on a continuous parameter such as _δ_, for instance, in systems subject to a time-periodic forcing, e.g., Kapitza's pendulum.9,10

**P3:** “_When cats are petted by people, they move back and forth in an oscillatory motion_.” This effect is also reproduced by the region of stability around _x_ = 0 (for δ\>0⁠). As Fig. 2(a) illustrates, when cats are calm and close to a person (low kinetic energy), they perform small-amplitude oscillations around the person, converging to the static state x\=ẋ\=0 (resting), thanks to the friction term in Eq. (1). As we explain in Sec. [VI](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#s6), the cat may display these stable oscillations even when petted by a stranger (_δ_ = 0), but for this, a new ingredient must be added (purring). Note that the motion observed in Fig. 2(a) is the one described by a damped oscillator, as can for instance be observed in the realization of the Cavendish experiment.11

Fig. 2.

![Image 6: Space-time representation of cat's trajectories with the values of the potential shown in color, white dashed lines mark the off-centered global minima and the black one the local minimum at x = 0. (a) Trajectory initially close to the person ( x(t=0)=0.15, ẋ(t=0)=0). (b) Trajectories from the minimum  (x(t=0)=xmin≈0.81) for two different initial velocities (see the label next to each curve). The cat–human bond has been set to  δ=0.25, the friction to  ϵ=0.1, and the mass to m = 1.](https://aipp.silverchair-cdn.com/aipp/content_public/journal/ajp/92/11/10.1119_5.0158200/1/m_827_1_5.0158200.figures.online.f2.jpeg?Expires=1734672380&Signature=yt90Nz0hs6gjPOZ77idw-HrpdKkDgSxPh24~D0cqfoIICoa2JAEM0awawZWmdfFgY3mdJflKF8BFEXWYNIjyDPL-BjwJX5HvFPKvSgPATsxG5K8mmXgn6MNJOH9iFoSEzQ2qE0TN3HeH8bfbuxJSs6QfDkgmrEy0Yt43jzviOZWTP8cVOu4c-Lnad5HJgjx3AhGFshUGa9lMdQSAW~VDrvq5Ywpe75vz7ztalA11-OqErS-wKL6iliDrktadT0xIttTtgXB0JPbm~yWxXghI1kRgfn8T4Ph8xTm7MP2pc2ZCL3P65gUjwRBeEMjR55gfxBTFbF3pLsJasaVepoGA0g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Space-time representation of cat's trajectories with the values of the potential shown in color, white dashed lines mark the off-centered global minima and the black one the local minimum at _x_ = 0. (a) Trajectory initially close to the person (⁠ x(t\=0)\=0.15, ẋ(t\=0)\=0⁠). (b) Trajectories from the minimum (x(t\=0)\=xmin≈0.81) for two different initial velocities (see the label next to each curve). The cat–human bond has been set to δ\=0.25⁠, the friction to ϵ\=0.1⁠, and the mass to _m_ = 1.

Fig. 2.

![Image 7: Space-time representation of cat's trajectories with the values of the potential shown in color, white dashed lines mark the off-centered global minima and the black one the local minimum at x = 0. (a) Trajectory initially close to the person ( x(t=0)=0.15, ẋ(t=0)=0). (b) Trajectories from the minimum  (x(t=0)=xmin≈0.81) for two different initial velocities (see the label next to each curve). The cat–human bond has been set to  δ=0.25, the friction to  ϵ=0.1, and the mass to m = 1.](https://aipp.silverchair-cdn.com/aipp/content_public/journal/ajp/92/11/10.1119_5.0158200/1/m_827_1_5.0158200.figures.online.f2.jpeg?Expires=1734672380&Signature=yt90Nz0hs6gjPOZ77idw-HrpdKkDgSxPh24~D0cqfoIICoa2JAEM0awawZWmdfFgY3mdJflKF8BFEXWYNIjyDPL-BjwJX5HvFPKvSgPATsxG5K8mmXgn6MNJOH9iFoSEzQ2qE0TN3HeH8bfbuxJSs6QfDkgmrEy0Yt43jzviOZWTP8cVOu4c-Lnad5HJgjx3AhGFshUGa9lMdQSAW~VDrvq5Ywpe75vz7ztalA11-OqErS-wKL6iliDrktadT0xIttTtgXB0JPbm~yWxXghI1kRgfn8T4Ph8xTm7MP2pc2ZCL3P65gUjwRBeEMjR55gfxBTFbF3pLsJasaVepoGA0g__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Space-time representation of cat's trajectories with the values of the potential shown in color, white dashed lines mark the off-centered global minima and the black one the local minimum at _x_ = 0. (a) Trajectory initially close to the person (⁠ x(t\=0)\=0.15, ẋ(t\=0)\=0⁠). (b) Trajectories from the minimum (x(t\=0)\=xmin≈0.81) for two different initial velocities (see the label next to each curve). The cat–human bond has been set to δ\=0.25⁠, the friction to ϵ\=0.1⁠, and the mass to _m_ = 1.

Close modal

Observations **P4** and **P5** are explained in terms of the potential barrier between an off-centered minimum and the person (_x_ = 0), see Fig. 1. **P4:** “_When cats are called by people, they seldom respond_.” The act of being called is modeled as an impulse of the cat toward the person, which results in an increment of the kinetic energy. This energy injection may be sufficient or insufficient to overcome the potential barrier, as illustrated by the blue (darker) and green (lighter) trajectories in Fig. 2(b), respectively. For an insufficient energy, the cat converges again to the resting position after some time, x\=xmin⁠. **P4** refers to the fact that cats often find the call to be so unmotivated that their interest is rapidly dissipated. In our model, this represents a very small increase of energy that is consumed by friction before the cat moves far. We see that cats need to experience a strong impulse to come to a person. This fact is often overlooked, provoking a feeling of frustration when the cat does not react to our call. This has generated the wrong idea that cats are “selfish” animals as Ref. 6 discusses, whereas cats just happen to have a stronger inner damping mechanism, compared to, say, dogs.

When the cat is given a sufficiently strong stimulus (impulse) to approach the person, we observe **P5:** “_When cats decide to approach the person who calls them, they often get distracted on the way and do not reach the person_.” This observation is also explained in terms of the damping mechanism described above, as illustrated by the green (lighter) trajectory in Fig. 2(b). It is interesting to discuss the role played by the cat's mass in this phenomenon. Since an external stimulus results in an injection of kinetic energy (_EK_), the velocity the cats acquire decreases with increasing the mass according to ẋ\=2EK/m⁠. It clearly aligns with the observation that light cats, such as kittens, exhibit energetic movements and react to any stimulus, while heavier cats, such as elderly or overfed cats, do not show the same enthusiasm. However, one must consider carefully the relation between the cat's mass (_m_) and friction (_ϵ_) to avoid unrealistic scenarios. To investigate this question, we write the cat's equation (Eq. (1)) in its dimensionless form,

d2x̃dτ2\=−dVcat(δ)(x̃)dx̃−ϵ̃dx̃dτ,

(5)

where τ\=t/m,  x̃(τ)\=x(t/m)⁠, and ϵ̃\=ϵ/m⁠. The energy variation takes the form

indicating that _ϵ_ must depend on _m_ to model cats of different masses. To illustrate this fact, let us assume that _ϵ_ is independent of _m_. In this situation, heavy cats would consume less energy than lighter ones because ϵ̃ decreases with _m_, i.e., elderly and overfed cats would not get tired, while kittens would be quickly exhausted (a world upside down!). This unrealistic situation is avoided by considering that the friction coefficient changes with the cat's mass. If _ϵ_ is proportional to m⁠, then cats would describe the same trajectory x̃(τ) independently of their mass. When the trajectory is expressed back in time t\=τm⁠, cats perform the same activity (they visit the same positions _x_) but require a shorter or longer time depending on their mass. We still believe this is not fully realistic, as kittens usually perform activities that are not displayed by elderly cats. We then conclude that the friction coefficient must grow faster than m⁠, e.g., ϵ∝m⁠, restoring the natural order of life where elderly cats (larger ϵ̃⁠) get exhausted more quickly than kittens (smaller ϵ̃⁠).

V. ZOOMIES AS A STOCHASTIC PROCESS
----------------------------------

Zoomies (**P6**), also known as frenetic random activity periods (FRAPs), are phases during which cats have an excess of energy that makes them suddenly run from place to place, usually at night. In our model, we assume that zoomies happen when the cat randomly moves between minima of Vcat(δ)⁠, representing long runs from one side of a room to the other. However, these random processes cannot be reproduced by our deterministic equation (Eq. (1)). If the cat has enough energy to move between minima of the potential, Eq. (1) predicts that this will not be a random process but will translate into repeated damped oscillations. At some point, the decreasing energy will not be sufficient to overcome the potential barrier for the cat to move to other minima. The best one can expect from deterministic systems is great sensitivity to initial conditions, in which case small variations in the conditions may lead to completely different trajectories (the so-called butterfly effect12). Even so, the energy would be consumed by friction, eventually impeding the displacement between minima. For these reasons, our deterministic setup requires an external forcing that randomly injects and extracts energy, producing a different trajectory each time the equation is solved for the same initial conditions. Namely, we turn the cat's equation into a stochastic equation.13 This approach is useful in systems that are subject to high uncertainty, such as the movement of suspended particles in a liquid (Brownian motion), which are subject to unpredictable collisions with the liquid particles.14

The stochastic cat's equation has the form

md2xdt2\=−dVcat(δ)(x)dx−ϵdxdt+σf(t),

(7)

where _σ_ is a constant and _f_(_t_) the external random forcing. This equation can be solved by numerical integration, using the Euler–Maruyama method,15 which is the Euler method adapted to stochastic equations.13 As _f_(_t_), we use white noise,13 a common phenomenon in physics, which is found in the aforementioned Brownian motion, or in more applied scenarios as in the dynamics of financial markets (e.g., Black–Scholes model13,16) As Fig. 3(a) illustrates, Eq. (7) produces zoomies: the cat may suddenly run from one equilibrium point to another, remain there for some time, and again randomly go back to the previous equilibrium point. The probability of producing zoomies in a given period of time depends on the values of the friction _ϵ_ and the forcing _σ_. This allows us to adjust the model to the particularities of each cat. For instance, kittens constantly exhibit these periods, corresponding to lower friction and higher forcing (Fig. 3(b)) than elderly cats, which rarely display such activity (Fig. 3(c)).

Fig. 3.

![Image 8: Space-time evolution of the stochastic cat's Eq. (7). The colored background represents the potential  Vcat(δ), the solid line the position of the cat, the white dashed lines the off-centered potential minima, and the black dashed line the origin. Green arrows in plot (a) mark zoomies, when the cat randomly runs from one minimum to another. In this plot, we used the following parameters:  (x(t=0),ẋ(t=0),δ,ϵ,m,σ)=(−0.9, 0, 0.25, 0.1, 1, 0.1). Plots (b) and (c) illustrate how friction and forcing have a great impact on the production of zoomies by using  (ϵ,σ)=(0.05,0.2) and  (ϵ,σ)=(0.2,0.095), respectively. Note that plot (c) presents an evolution eight times longer than (a) and (b).](https://aipp.silverchair-cdn.com/aipp/content_public/journal/ajp/92/11/10.1119_5.0158200/1/m_827_1_5.0158200.figures.online.f3.jpeg?Expires=1734672380&Signature=wO9tYBXL0helZVccQZKTHMY8XUb1fmxo3-hlfynXshVKmvX0zANNOYX36PlFVQk8ZwIg8M2nF8QG5FOm1qt8TaOWF-z5q3KIUUt3-9964dLAVJY~A~oPgkBXebsGu7u~g8YIvAUlSpXILTnsOpYrfl9jtkAu2CV8g77uHzgKQ4jLZt4wjaRya7ZLVkWA~kEtEuzpAGCgKcKPfJyPSo5RHPlOzQbz2wxxkyDAnGyVAAUg1zXbRNl1pUGpGDXmdCdvsVEDe2TCndR9MjwW2OW23MDDubQLDrMCNIOlzDlH4FwKm5dtRlQK7h~-KuncihpV0C0J7X5sEK9HZzgBuQDv7w__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Space-time evolution of the stochastic cat's Eq. (7). The colored background represents the potential Vcat(δ)⁠, the solid line the position of the cat, the white dashed lines the off-centered potential minima, and the black dashed line the origin. Green arrows in plot (a) mark zoomies, when the cat randomly runs from one minimum to another. In this plot, we used the following parameters: (x(t\=0),ẋ(t\=0),δ,ϵ,m,σ)\=(−0.9, 0, 0.25, 0.1, 1, 0.1)⁠. Plots (b) and (c) illustrate how friction and forcing have a great impact on the production of zoomies by using (ϵ,σ)\=(0.05,0.2) and (ϵ,σ)\=(0.2,0.095)⁠, respectively. Note that plot (c) presents an evolution eight times longer than (a) and (b).

Fig. 3.

![Image 9: Space-time evolution of the stochastic cat's Eq. (7). The colored background represents the potential  Vcat(δ), the solid line the position of the cat, the white dashed lines the off-centered potential minima, and the black dashed line the origin. Green arrows in plot (a) mark zoomies, when the cat randomly runs from one minimum to another. In this plot, we used the following parameters:  (x(t=0),ẋ(t=0),δ,ϵ,m,σ)=(−0.9, 0, 0.25, 0.1, 1, 0.1). Plots (b) and (c) illustrate how friction and forcing have a great impact on the production of zoomies by using  (ϵ,σ)=(0.05,0.2) and  (ϵ,σ)=(0.2,0.095), respectively. Note that plot (c) presents an evolution eight times longer than (a) and (b).](https://aipp.silverchair-cdn.com/aipp/content_public/journal/ajp/92/11/10.1119_5.0158200/1/m_827_1_5.0158200.figures.online.f3.jpeg?Expires=1734672380&Signature=wO9tYBXL0helZVccQZKTHMY8XUb1fmxo3-hlfynXshVKmvX0zANNOYX36PlFVQk8ZwIg8M2nF8QG5FOm1qt8TaOWF-z5q3KIUUt3-9964dLAVJY~A~oPgkBXebsGu7u~g8YIvAUlSpXILTnsOpYrfl9jtkAu2CV8g77uHzgKQ4jLZt4wjaRya7ZLVkWA~kEtEuzpAGCgKcKPfJyPSo5RHPlOzQbz2wxxkyDAnGyVAAUg1zXbRNl1pUGpGDXmdCdvsVEDe2TCndR9MjwW2OW23MDDubQLDrMCNIOlzDlH4FwKm5dtRlQK7h~-KuncihpV0C0J7X5sEK9HZzgBuQDv7w__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Space-time evolution of the stochastic cat's Eq. (7). The colored background represents the potential Vcat(δ)⁠, the solid line the position of the cat, the white dashed lines the off-centered potential minima, and the black dashed line the origin. Green arrows in plot (a) mark zoomies, when the cat randomly runs from one minimum to another. In this plot, we used the following parameters: (x(t\=0),ẋ(t\=0),δ,ϵ,m,σ)\=(−0.9, 0, 0.25, 0.1, 1, 0.1)⁠. Plots (b) and (c) illustrate how friction and forcing have a great impact on the production of zoomies by using (ϵ,σ)\=(0.05,0.2) and (ϵ,σ)\=(0.2,0.095)⁠, respectively. Note that plot (c) presents an evolution eight times longer than (a) and (b).

Close modal

VI. PURRING: A STABILIZATION MECHANISM
--------------------------------------

**P7:** “_Cats purr (emit a soft and vibrating sound) when they like being petted by a person_.” In this section, we propose that purring is a stabilization mechanism. First, we point out that when a cat is being petted and begins purring, people generally get the urge to keep petting the cat, strengthening in this way the stability of the process. The second reason is the analogy with Kapitza's pendulum.9,17 While the inverted pendulum is normally unstable, it may become stable by introducing vibrations (small-amplitude high-frequency oscillations) in the vertical direction. Vibrations then work as a stabilization mechanism for unstable equilibrium points. This is exactly the model we propose for purring: that vibrations strengthen the effective bond between cat and human.

Noting that cats vibrate when they purr (as can be checked by placing a hand on their back), we introduce an external vibrating forcing in the cat's Eq. (1) to mimic the effect,

md2xdt2\=−dVcat(δ)(x)dx−ϵdxdt+βΩ2G(x) cos(Ωt),

(8)

where _G_(_x_) is an unconstrained function for now, and _β_ and Ω are the amplitude and frequency of the vibrations induced in the cat, respectively. Driving terms of this kind model a particle moving in an oscillating field in time or subject to periodic forcing.10 The typical example is Kapitza's pendulum,9,17 where G(θ) is proportional to dVg/dθ⁠, with _Vg_ being the gravitational potential and replacing _x_ by the angular coordinate _θ._17 We choose β≪1⁠, and Ω≫1 with βΩ∼O(1) in order to reproduce the small-amplitude high-frequency vibrations that are observed when purring. The goal is to determine the conditions that _G_(_x_) must satisfy in order to replicate the effect of purring on the cat–human bond.

The equation contains high-frequency oscillatory terms superposed to the original potential Vcat(δ)⁠. This means that the solutions get contributions at two time scales, t∼O(Ω−1) associated with the fast vibrations, and t∼O(1) associated with the average motion of the cat, as we show by numerically solving the equation (Fig. 4(b)). The latter motion may be obtained by averaging the trajectory over a period of fast oscillations,

x¯(t)≡Ω2π∫t−π/Ωt+π/Ωx(s)ds.

(9)

Decomposing the dynamics in slow and fast motions and using an averaging method (see  [Appendix](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#app1) for details), the average (or slow) motion of _x_(_t_), denoted by x¯(t)⁠, is approximated by the trajectory of a cat submitted to a time-independent effective potential of the form

Ueff(x¯)\=Vcat(δ)(x¯)+(βΩ)24mG(x¯)2.

(10)

The equilibrium points of this potential now depend on Vcat(δ)(x¯) and G(x¯)⁠, indicating that the amplitude of the external forcing plays an important role. An analysis at the origin, the point relevant to us, reveals that G(x\=0)G′(x\=0)\=0 and G′(x\=0)2+G(x\=0)G″(x\=0)\>0 are required to maintain the person's position as an equilibrium point and to enhance its stability during purring. As an example, G\=dVcat(δ)/dx satisfies these conditions, maintaining the original equilibrium points, but their stability/instability may change depending on the product βΩ⁠,

d2Ueffdx¯2|x¯\=0\={−2+2(βΩ)2mif δ\=0,2+2(βΩ)2mif δ\>0.

(11)

The unstable point _x_ = 0 for _δ_ = 0 turns into a stable one when βΩ\>m1/2 (see Fig. 4(c)), indicating that introducing external vibrations in our model has similar effects on the stability of _x_ = 0 as increasing _δ_. For δ\>0⁠, _x_ = 0 is already stable, but the stability is strengthened with the growth of βΩ⁠, in the sense that Ueff grows from the origin faster than Vcat(δ) (see Fig. 4(d)). Thus, for the same energy, displacements from the origin have a smaller amplitude when forcing is introduced, indicating that the cat has a stronger effective attachment to the person. These observations suggest that cats purr to temporarily strengthen the bond with humans, using vibrations to evoke a feeling that makes people want to keep petting them.

Fig. 4.

![Image 10: (a) Comparison between trajectories as given by the cat's equation with and without external vibration, both initiated with the same initial conditions ( x(t=0)=0.1, ẋ(t=0)=0), δ = 0, and  ϵ=0.1. Equilibrium points are marked by black dashed lines. (b) A closer view of the trajectory subject to external vibrations shown in plot (a) and its average motion. (c) Potential  Vcat(δ) vs effective potential  Ueff for δ = 0. (d) Potential  Vcat(δ) vs effective potential  Ueff for  δ=0.25. We fixed m = 1 in these plots.](https://aipp.silverchair-cdn.com/aipp/content_public/journal/ajp/92/11/10.1119_5.0158200/1/m_827_1_5.0158200.figures.online.f4.jpeg?Expires=1734672380&Signature=SnWzG1NUin8TmjjsEHO23F7LcrBLiWGZnf7A3nN~qpQ9kjNmDB4E5WtwvxmCoT8Zt~Aw7r4-CUI-sXdUTONM2flex3KXY019FD06znsTT5QNQH6DI8va089YQR0vKGy02ZRdv7kgdfTla~XDgieXU6r0xo2YZobSlNjJP5Rw2wCTsttJZtlRFWHpJBmau91pI7PiHAMwGJD4tDRBXZamjqBxaezw~6twV5PRyit42nUBcL0kg7sSJQBjbuqR4Z-K6E8KPZkkVpbtt1wIF2otou6veGBE8hEgy9hJ07Zf6hksxiJJXXNi-IAF9t20ymja2yUtXC62vpNidy-WGIQ3PA__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

(a) Comparison between trajectories as given by the cat's equation with and without external vibration, both initiated with the same initial conditions (⁠ x(t\=0)\=0.1, ẋ(t\=0)\=0⁠), _δ_ = 0, and ϵ\=0.1⁠. Equilibrium points are marked by black dashed lines. (b) A closer view of the trajectory subject to external vibrations shown in plot (a) and its average motion. (c) Potential Vcat(δ) vs effective potential Ueff for _δ_ = 0. (d) Potential Vcat(δ) vs effective potential Ueff for δ\=0.25⁠. We fixed _m_ = 1 in these plots.

Fig. 4.

![Image 11: (a) Comparison between trajectories as given by the cat's equation with and without external vibration, both initiated with the same initial conditions ( x(t=0)=0.1, ẋ(t=0)=0), δ = 0, and  ϵ=0.1. Equilibrium points are marked by black dashed lines. (b) A closer view of the trajectory subject to external vibrations shown in plot (a) and its average motion. (c) Potential  Vcat(δ) vs effective potential  Ueff for δ = 0. (d) Potential  Vcat(δ) vs effective potential  Ueff for  δ=0.25. We fixed m = 1 in these plots.](https://aipp.silverchair-cdn.com/aipp/content_public/journal/ajp/92/11/10.1119_5.0158200/1/m_827_1_5.0158200.figures.online.f4.jpeg?Expires=1734672380&Signature=SnWzG1NUin8TmjjsEHO23F7LcrBLiWGZnf7A3nN~qpQ9kjNmDB4E5WtwvxmCoT8Zt~Aw7r4-CUI-sXdUTONM2flex3KXY019FD06znsTT5QNQH6DI8va089YQR0vKGy02ZRdv7kgdfTla~XDgieXU6r0xo2YZobSlNjJP5Rw2wCTsttJZtlRFWHpJBmau91pI7PiHAMwGJD4tDRBXZamjqBxaezw~6twV5PRyit42nUBcL0kg7sSJQBjbuqR4Z-K6E8KPZkkVpbtt1wIF2otou6veGBE8hEgy9hJ07Zf6hksxiJJXXNi-IAF9t20ymja2yUtXC62vpNidy-WGIQ3PA__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

(a) Comparison between trajectories as given by the cat's equation with and without external vibration, both initiated with the same initial conditions (⁠ x(t\=0)\=0.1, ẋ(t\=0)\=0⁠), _δ_ = 0, and ϵ\=0.1⁠. Equilibrium points are marked by black dashed lines. (b) A closer view of the trajectory subject to external vibrations shown in plot (a) and its average motion. (c) Potential Vcat(δ) vs effective potential Ueff for _δ_ = 0. (d) Potential Vcat(δ) vs effective potential Ueff for δ\=0.25⁠. We fixed _m_ = 1 in these plots.

Close modal

Similar stability in periodically driven systems is observed in other contexts. In quantum many-body physics, the topic has been under intense research in the last decades,18,19 both theoretically and experimentally. It has been shown that periodic driving may be particularly useful to manipulate systems, for instance, it allows to reach new phases of matter such as topological insulators.20

VII. CONCLUSIONS
----------------

We have explored cat–human interaction from the viewpoint of physics. We first identified seven characteristic dynamics a cat displays in the presence of a person at rest (**P1**–**P7**). Considering the cat as a point particle moving in a potential induced by the person, we presented an equation of motion (Eq. (1)) that reproduces these behaviors. With this first approximation to the cat–human interaction, we have built a qualitative picture that reflects the way cats perceive the presence of people, something that can be visualized by simply plotting a potential. This work establishes an arena to explore other features of cat–human interactions from the viewpoint of physics, such as the presence of several people, or even addressing new scenarios such as cat–cat, dog–dog, or dog–human interactions.

The cat–human interaction model we have introduced is intended to be used in introductory courses in classical mechanics to familiarize students with notions such as equilibrium points, potential barriers, friction, or external forcing. The model has three aspects that would benefit the exposition of concepts: (1) a low level of abstraction, (2) a collection of real-world dynamics (cat behavior) that facilitates visualization of results, and (3) a curious story that calls the attention of students. For these reasons, we believe that the model would help students to assimilate concepts while they see, at the same time, that physics may be used in an enjoyable way.

ACKNOWLEDGMENTS
---------------

The author is grateful to his cat for being his source of inspiration. The author also thanks Paloma Calderón Bustillo, Brad Cownden, Piotr Bizoń, and Ángel Paredes for useful discussions. During the development of this work, the author has been supported by the LabEx ENS-ICFP: ANR-10-LABX-0010/ANR-10-IDEX-0001-02 PSL\*.

AUTHOR DECLARATIONS
-------------------

### Conflict of Interest

The author has no conflicts to disclose.

### Ethics Approval

This work is for educational purposes in physics and must not be understood as research on cat or human behavior. Furthermore, no experiments on animal or human subjects have been conducted to develop this work.

### APPENDIX: AVERAGING APPROXIMATION

We describe the procedure10 followed in Sec. [VI](https://pubs.aip.org/aapt/ajp/article/92/11/827/3317285/On-cat-human-interaction-from-the-viewpoint-of#s6) to construct an approximation of the solution to the cat's equation under external vibrating forcing (8),

md2xdt2\=−dVcat(δ)(x)dx−ϵdxdt+βΩ2G(x) cos(Ωt),

(A1)

where _G_(_x_) is an unconstrained function for now, β≪1 and Ω≫1 with βΩ∼O(1)⁠. We proceed perturbatively by introducing the small parameter ξ≪1 such that

with β̃, Ω̃∼O(1)⁠. The solution is then decomposed in the form

with y, z∼O(1)⁠. The first term represents the leading part of the fast evolution (i.e., small-amplitude high-frequency oscillations), while _y_ contains the slow evolution and subleading terms of the fast motion. This separation will allow us to first obtain an expression for _z_, followed by an effective equation for the average motion of _y_. Note that highly oscillatory terms in _y_ cannot be neglected at this point because they will appear in the equation for _y_; that is why we need an averaging. Note as well that differentiation of ξz(t/ξ) increases its order (⁠ τ:\=t/ξ⁠),

ξd2z(t/ξ)dt2\=ξ−1d2z(τ)dτ2∼O(ξ−1).

(A5)

Plugging (A3) into Eq. (A1) and gathering terms of the same order in _ξ_, we get that the leading order equation is

md2zdτ2\=β̃Ω̃2G(y) cos(Ω̃τ),

(A6)

while the next order equation is

md2ydt2\=−dVcat(δ)(y)dy−ϵ(dydt+dzdτ)+dG(y)dyzβ̃Ω̃2 cos(Ω̃τ).

(A7)

The solution to Eq. (A6) can be approximated at leading order by

z(τ)≈−m−1β̃G(y) cos(Ω̃τ).

(A8)

We used the fact that _y_(_t_) has two motions: subleading fast oscillations, which we neglected in the expression, and the slow motion that evolves on the time scale t∼O(1)⁠. The latter remains practically constant when the equation is integrated over _τ_ (⁠ t∼O(ξ)⁠), namely, in an interval of order _ξ_. Therefore, one may perform the integration of Eq. (A6) considering _G_(_y_) as a constant. See Ref. 21 for the details of this approximation. The intuitive idea comes from the fact that, to leading order,

∫t0t0+ξτf(t) sin(Ω̃tξ)dt≈f(t0)∫t0t0+ξτ sin (Ω̃tξ)dt,

(A9)

when _f_(_t_) is a function evolving over time scales t∼O(1)⁠.

Plugging the expression for z(τ) in Eq. (A7), one gets a right-hand side with terms that evolve with a typical time scale _t_ but also highly oscillatory terms in _τ_. To get the slow evolution of _y_(_t_), we average the motion over periods of the fast oscillations similar to what we did in Eq. (9), getting ⟨sin(Ω̃τ)⟩\=0 and ⟨cos2(Ω̃τ)⟩\=1/2⁠. With that, an equation for the average motion y¯(t)\=⟨y(t)⟩ is obtained,

md2y¯dt2\=−dVcat(δ)(y¯)dy−(β̃Ω̃)22mG(y¯)dG(y¯)dy−ϵdy¯dt,

(A10)

from which we infer that the effective potential has the form

Ueff(y¯)\=Vcat(δ)(y¯)+(βΩ)24mG(y¯)2.

(A11)

REFERENCES
----------

1.

T. R.

Kane

andM. P.

Scher

, “

A dynamical explanation of the falling cat phenomenon

,”

Int. J. Solids Struct.

5

(

7

),

663

–

670

(

1969

).

2.

F.

Studnička

,J.

Šlégr

, andD.

Štegner

, “

Free fall of a cat–freshman physics exercise

,”

Eur. J. Phys.

37

(

4

),

045002

(

2016

).

3.

J. H.

Challis

, “

The mechanics of a cat landing from a drop

,”

Eur. J. Phys.

44

(

1

),

015001

(

2022

).

4.

F.

Ornek

,W. R.

Robinson

, andM. P.

Haugan

, “

What makes physics difficult?

,”

Int. J. Environ. Sci. Educ.

3

,

30

–

34

(

2008

).

5.

D. C.

Turner

, “

A review of over three decades of research on cat-human and human-cat interactions and relationships

,”

Behav. Processes

141

,

297

–

304

(

2017

).

6.

K. R.

Vitale Shreve

andM. A.

Udell

, “

What's inside your cat's head? A review of cat (Felis silvestris catus) cognition research past, present and future

,”

Anim. Cogn.

18

(

6

),

1195

–

1206

(

2015

).

7.

J.

Weiner

,V. S.

Bagnato

,S.

Zilio

, andP. S.

Julienne

, “

Experiments and theory in cold and ultracold collisions

,”

Rev. Mod. Phys.

71

(

1

),

1

–

85

(

1999

).

8.

A.

Picozzi

,J.

Garnier

,T.

Hansson

,P.

Suret

,S.

Randoux

,G.

Millot

, andD. N.

Christodoulides

, “

Optical wave turbulence: Towards a unified nonequilibrium thermodynamic formulation of statistical nonlinear optics

,”

Phys. Rep.

542

(

1

),

1

–

132

(

2014

).

9.

P. L.

Kapitza

, “

Dynamic stability of a pendulum with an oscillating point of suspension

,”

J. Exp. Theor. Phys.

21

,

588

–

597

(

1951

).

10.

L. D.

Landau

andE. M.

Lifshitz

, “

Chapter 5.30: Motion in a rapidly oscillating field

,”

_Mechanics_

(

Elsevier

,

1982

), Vol.

1

.

11.

Y. T.

Chen

andA.

Cook

, “

Chapter 8: The constant of gravitation

,”

_Gravitational Experiments in the Laboratory_

(

Cambridge U. P

.,

1993

).

12.

J.

Gleick

, “

Chapter 1: The Butterfly Effect

,”

_Chaos: Making of a New Science_

(

Viking Penguin

,

1987

).

13.

S.

Särkkä

andA.

Solin

, “

Chapter 3: Pragmatic introduction to stochastic differential equations

,”

_Applied Stochastic Differential Equations_

(

Cambridge U. P

.,

2019

).

14.

R.

Feynman

,R.

Leighton

, andM.

Sands

, “

The Brownian movement

,” in

_The Feynman Lectures on Physics_

(Addison—Wesley, 1964), Vol. I.

15.

M.

Bayram

,T.

Partal

, andG.

Orucova Buyukoz

, “

Numerical methods for simulation of stochastic differential equations

,”

Adv. Differ. Equations

2018

,

17

.

16.

Y. H. A.

Saedi

andG.

Tularam

, “

A review of the recent advances made in the Black-Scholes models and respective solutions methods

,”

J. Math. Stat.

14

(

1

),

29

–

39

(

2018

).

17.

E. I.

Butikov

, “

On the dynamic stabilization of an inverted pendulum

,”

Am. J. Phys.

69

(

7

),

755

–

768

(

2001

).

18.

M.

Bukov

,Luca

D'Alessio

, andA.

Polkovnikov

, “

Universal high-frequency behavior of periodically driven systems: From dynamical stabilization to Floquet engineering

,”

Adv. Phys.

64

(

2

),

139

–

226

(

2015

).

19.

A.

Eckardt

, “

Colloquium: Atomic quantum gases in periodically driven optical lattices

,”

Rev. Mod. Phys.

89

(

1

),

011004

(

2017

).

20.

M. C.

Rechtsman

,J. M.

Zeuner

,Y.

Plotnik

,Y.

Lumer

,D.

Podolsky

,F.

Dreisow

,S.

Nolte

,M.

Segev

, andA.

Szameit

, “

Photonic Floquet topological insulators

,”

Nature

496

(

7444

),

196

–

200

(

2013

).

21.

J. A.

Murdock

, “

Chapter 6: Averaging

,”

_Perturbations: Theory and Methods_

(

Wiley

,

New York

,

1991

).

© 2024 Author(s). Published under an exclusive license by American Association of Physics Teachers.

2024

Author(s)

