---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I received my Ph.D. degree from National University of Defense Technology (NUDT) in 2026. During my Ph.D. study, I was fortunate to be supervised by Prof. Xinjun Mao and co-supervised by [Prof. Yue Yu](https://yuyue.github.io/). I received the bachelor's degree from Tsien Hsue-shen Class, NUDT, in June 2020. My research interests include AI4SE, code reuse, code snippet adaptation, and empirical software engineering.


# 🔥 News
- *2026.09*: 🎉🎉 Our paper about *Logical Context Enhanced Code Generation (LogiCoder)* was accepted by **TOSEM** after major revision! This is the final part of my Ph.D dissertation!
- *2026.07*: 🎉🎉 Our paper about *Block-aware Code Differencing* was accepted by **ASE 2026** after major revision! Congrats to Prof. Lu and Prof. Liu!
- *2026.05*: &nbsp;🎉🎉I have successfully defended my PhD dissertation!
- *2026.04*: &nbsp;🎉🎉 Our paper about *Deprecated NPM Packages* was directly accepted by **ISSTA 2026** (10.1%)! This is the first **ISSTA** paper in our group! Congrats to Zezhou!
- *2025.12*: &nbsp;🎉🎉 Our paper about *Context Adaptation Bug Resolution* was directly accepted by **FSE 2026** (9.4%)! This is the first **FSE** paper in our group!
- *2025.09*: &nbsp;🎉🎉 Our paper about *Code Adaptation Benchmark (AdaptEval)* was accepted by **ASE 2025** after major revision! This is the first **ASE** paper in our group!
- *2025.04*: &nbsp;🎉🎉 Thrilled to announce our ICPC paper won 🏆<span style="color:red">***ACM SIGSOFT Distinguished Paper Award***</span>!
- *2024.10*: &nbsp;🎉🎉 Our paper about *LLM-based Code Adaptation* was directly accepted by **ICSE 2025** (10.3%)! This is the first **CCF-A** SE conference paper in our group!


# 📝 Publications 

## Representative Works

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">FSE 2026</div><img src='images/FSE-26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Coding in a Bubble? Evaluating LLMs in Resolving Context Adaptation Bugs During Code Adaptation](https://arxiv.org/abs/2601.06497)



**Tanghaoran Zhang**, Xinjun Mao, Shangwen Wang, Yuxin Zhao, Yao Lu, Zezhou Tang, Wenyu Xu, Longfei Sun, Changrong Xie, Kang Yang and Yue Yu.

**FSE 2026** (<span style="color:red">**CCF-A**</span>)

[**Project**](https://github.com/ztwater/CtxBugGen)

- We propose ***CtxBugGen***, a novel framework for generating *CtxBugs* through a four-step process: (1) Task Selection, (2) Syntax-based Perturbation, (3) LLM-based Variant Generation and (4) Hybrid Identification. Based on ***CtxBugGen***, we reveal LLMs' unsatisfactory performance in *CtxBug* resolution, highlighting their preference for local code correctness and critical weakness in cross-context reasoning.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TOSEM 2026</div><img src='images/TOSEM-26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[LLM See, LLM Do: Enhancing Repository-Aware Code Generation in LLMs Through Logical Context and Usage Knowledge](https://ztwater.github.io)



**Tanghaoran Zhang**, Xinjun Mao, Yuxin Zhao, Kang Yang, Zhang Zhang, Yao Lu, Youren Chen and Yue Yu.

**TOSEM 2026** (<span style="color:red">**CCF-A**</span>)

[**Project**](https://github.com/ztwater/LogiCoder)

- We propose **LogiCoder**, a novel RAG approach that leverages logical relationships to improve LLMs’ repository awareness during code generation. Using a repository-level dependency graph, it retrieves candidate callees and their most contextually similar usage examples, then re-ranks them with semantic search results.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ASE 2025</div><img src='images/ASE-25.png' alt="sym" width="100%"></div></div>

<div class='paper-box-text' markdown="1">
[AdaptEval: A Benchmark for Evaluating Large Language Models on Code Snippet Adaptation](https://arxiv.org/abs/2601.04540)


**Tanghaoran Zhang**, Xinjun Mao, Shangwen Wang, Yuxin Zhao, Yao Lu, Jin Zhang, Zhang Zhang, Kang Yang and Yue Yu.

**ASE 2025** (<span style="color:red">**CCF-A**</span>)

[**Project**](https://github.com/ztwater/AdaptEval) \| [**Video**](https://www.bilibili.com/video/BV1JX1aBTED8)

- We construct ***AdaptEval***, the first benchmark for evaluating LLM-based code snippet adaptation. It incorporates three distinctive features:  (1) *practical context* derived from developers’ reuse practices; (2) *multi-granularity annotations* supporting evaluation across diverse adaptation scenarios; (3) *fine-grained evaluation* supporting evaluation across various individual adaptations.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICSE 2025</div><img src='images/ICSE-25.png' alt="sym" width="100%"></div></div>

<div class='paper-box-text' markdown="1">
[Instruct or Interact? Exploring and Eliciting LLMs’ Capability in Code Snippet Adaptation Through Prompt Engineering](https://ieeexplore.ieee.org/document/11029912)


**Tanghaoran Zhang**, Yue Yu, Xinjun Mao, Shangwen Wang, Kang Yang, Yao Lu, Zhang Zhang and Yuxin Zhao.

**ICSE 2025** (<span style="color:red">**CCF-A**</span>)

[**Project**](https://github.com/ztwater/Instruct-or-Interact) 

- We first empirically investigate the capability of LLMs on the code adaptation task and find the root causes of their sub-optimal performance: (1) Unclear Requirement, (2) Requirement Misalignment and (3) Context Misapplication. To resolve above issues, we propose an interactive prompting approach to eliciting LLMs’ ability in code snippet adaptation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TSE 2024</div><img src='images/TSE-24.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[How Do Developers Adapt Code Snippets to Their Contexts? An Empirical Study of Context-Based Code Snippet Adaptations](https://ieeexplore.ieee.org/document/10510659)

**Tanghaoran Zhang**, Yao Lu, Yue Yu, Xinjun Mao, Yang Zhang and Yuxin Zhao.

**TSE** (<span style="color:red">**CCF-A**</span>, SCI-Q1),  **2024**

[**Project**](https://github.com/ztwater/how_to_adapt_code_snippet) 

- We investigate how developers adapt code snippets to their project context based on a semi-structured interview and a quantitative study on 300 real-world adaptation cases. We point out current challenges in the adaptation practices and obtain four typical context-based adaptation patterns. 
</div>
</div>

----

- [FENSE: A Feature-based Ensemble Modeling Approach to Cross-project Just-in-time Defect Prediction](https://link.springer.com/article/10.1007/s10664-022-10185-8), **Tanghaoran Zhang**, Yue Yu, Xinjun Mao, Yao Lu, Zhixing Li and Huaimin Wang, **EMSE** (CCF-B, JCR-Q1), **2022**

## All Publications
- [Detecting Evasive Benchmark Contamination in Code Generation by Mutating Code-Behavior Units](https://ztwater.github.io), Menghan Wu, Xing Hu, **Tanghaoran Zhang** and Shanping Li,  **APSEC 2026** (CCF-C).
- [BDiff: Block-aware and Accurate Text-based Code Differencing](https://ztwater.github.io), Yao Lu, Wanwei Liu, **Tanghaoran Zhang**, Kang Yang, Yang Zhang, Wenyu Xu, Longfei Sun, Xinjun Mao, Shuzheng Gao and Michael R Lyu, **ASE 2026** (<span style="color:red">***CCF-A***</span>).
- [Evaluating LLMs in ROS Robotic Software Code Generation](https://ztwater.github.io), Yuxin Zhao, Xinjun Mao, **Tanghaoran Zhang**, Tun Li and Zhiqun Xiao, **EMSE 2026** (CCF-B).
- [Deprecated but Not Abandoned: A Large-Scale Empirical Study on Growing-user-demand Deprecated NPM Packages](https://ztwater.github.io), Zezhou Tang, Yang Zhang, Xinjun Mao, **Tanghaoran Zhang**, Changrong Xie, Wenyu Xu, Simeng Yao and Yiwen Wu, **ISSTA 2026** (<span style="color:red">***CCF-A***</span>).
- [ConflictLens: An LLM-Based Method for Detecting Semantic Merge Conflicts](https://ztwater.github.io), Longfei Sun, Yao Lu, Xinjun Mao, **Tanghaoran Zhang**, Zhang Zhang and Huiping Zhou, **SEKE 2025** (CCF-C).
- [Understanding the Faults in Serverless Computing Based Applications: An Empirical Study](https://ztwater.github.io), Changrong Xie, Yang Zhang, Xinjun Mao, Kang Yang and **Tanghaoran Zhang**, **ICSME 2025** (CCF-B).
- [CARLDA: An Approach for Stack Overflow API Mention Recognition Driven by Context and LLM-based Data Augmentation](https://onlinelibrary.wiley.com/doi/10.1002/smr.70015), Zhang Zhang, Xinjun Mao, Shangwen Wang, Kang Yang, **Tanghaoran Zhang** and Yao Lu, **JSEP** (CCF-B), **2025**.
- [Large Language Models are Qualified Benchmark Builders: Rebuilding Pre-Training Datasets for Advancing Code Intelligence Tasks](https://ieeexplore.ieee.org/document/11025927), Kang Yang, Xinjun Mao, Shangwen Wang, Yanlin Wang, **Tanghaoran Zhang**, Bo Lin, Yihao Qin, Zhang Zhang, Yao Lu and Kamal Al-Sabahi, **ICPC 2025** (CCF-B),  🏆<span style="color:red">***ACM SIGSOFT Distinguished Paper Award***</span>.
- [Improving API Knowledge Comprehensibility: A Context-Dependent Entity Detection and Context Completion Approach Using LLM](https://ieeexplore.ieee.org/document/10992400), Zhang Zhang, Xinjun Mao, Shangwen Wang, Kang Yang, **Tanghaoran Zhang**, Fei Gao and Xunhui Zhang, **SANER 2025** (CCF-B).
- [An Empirical Study of Cross-Project Pull Request Recommendation in GitHub](), Wenyu Xu, Yao Lu, Xunhui Zhang, **Tanghaoran Zhang**, Bo Lin and Xinjun Mao, **APSEC 2024** (CCF-C).
- [MUSE: A Multi-Feature Semantic Fusion Method for ROS Node Search Based on Knowledge Graph](), Yuxin Zhao, Xinjun Mao, **Tanghaoran Zhang** and Zhang Zhang, **APSEC 2023** (CCF-C).
- [An Effective Method for Constructing Knowledge Graph to Search Reusable ROS Nodes](), Yuxin Zhao, Xinjun Mao, Sun Bo, **Tanghaoran Zhang** and Shuo Yang, **SEKE 2023** (CCF-C).
- [An Extensive Study of the Structure Features in Transformer-based Code Semantic Summarization](https://ieeexplore.ieee.org/document/10174079), Kang Yang, Xinjun Mao, Shangwen Wang, Yihao Qin, **Tanghaoran Zhang**, Yao Lu and Kamal Al-Sabahi, **ICPC 2023** (CCF-B).
- [Verifying ReLU Neural Networks from a Model Checking Perspective](https://link.springer.com/article/10.1007/s11390-020-0546-7), Wanwei Liu, Fu Song, **Tanghaoran Zhang** and Ji Wang, **JCST** (CCF-B), **2020**.

# 🎖 Honors and Awards
- *2025.11*, 💰First-Prize Merit Scholarship, NUDT.
- *2025.04*, 🏆ACM SIGSOFT Distinguished Paper Award in ICPC 2025.
- *2023.03*, 💰Second-Prize Merit Scholarship, NUDT.
- *2020.05*, 💰Qiangjun Scholarship, NUDT.
- *2019.10*, 🏅Outstanding Winner of M* Modeling Contest.
- *2019.10*, 🏆CCF Outstanding Undergraduate, CCF.
- *2019.05*, 💰Yinhe Scholarship, College of Computer Science and Technology, NUDT.
- *2019.05*, 🏅Meritorious Winner of MCM/ICM.
- *2018.05*, 🏅Meritorious Winner of MCM/ICM.

# 📖 Educations
- *2020.09 - 2026.06*, National University of Defense Technology (NUDT), Ph.D. in Software Engineering. 
- *2016.09 - 2020.06*, Tsien Hsue-shen Class (**1/30**), National University of Defense Technology (NUDT), B.E. in Software Engineering. 
- *2010.09 - 2016.06*, The High School Affiliated to Renmin University of China (RDFZ), Middle and High School.

# ⚙️ Services
- **Program Committee**
  - ICSE'26 Shadow PC

- **Reviewer**
  - TSE, EMSE, KAIS
- **External Reviewer**
  - Journal: TSE, TOSEM, EMSE, JCST, JoS
  - Conference: FSE'26, SANER'26, ICLR'25, ASE'24, ESEM'24

# 💬 Invited Talks
- *2026.04*, FSE 2026 Paper Pre-conference Presentation \| [Video](https://weixin.qq.com/sph/AOHbTcCdXf).
- *2025.11*, ASE 2025 Paper Pre-conference Presentation \| [Video](https://www.bilibili.com/video/BV1JX1aBTED8).
- *2024.12*, ICSE 2025 Paper Pre-conference Presentation \| [Video](https://www.bilibili.com/video/BV1RhBjYgEJs).

# 💻 Internships
- *2025.03 - 2025.10*, Visiting student at Peng Cheng Laboratory, Shenzhen, Guangdong.
- *2019.07 - 2019.10*, Mitacs Research Internship, at [SEAL](https://seal-queensu.github.io) in Queen's University, Canada, supervised by Prof. Ying Zou.
