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

I am currently a Ph.D. student in National University of Defense Technology (NUDT). I am supervised by Prof. Xinjun Mao and co-supervised by Prof. Yue Yu. I received the bachelor's degree from Tsien Hsue-shen Class, NUDT, in June 2020. My research interests include AI/LLM4SE, code reuse, code snippet adaptation, and empirical software engineering.


# 🔥 News
- *2025.06*: &nbsp;🎉🎉 One paper accepted to **ICSME 2025**. 
- *2025.04*: &nbsp;🎉🎉 Thrilled to announce our ICPC paper won <span style="color:red">***ACM SIGSOFT Distinguished Paper Award***</span>!
- *2025.01*: &nbsp;🎉🎉 One paper was accepted by **ICPC 2025**. 
- *2024.12*: &nbsp;🎉🎉 One paper was accepted by **SANER 2025**. 
- *2024.10*: &nbsp;🎉🎉 Our paper about *LLM-based Code Adaptation* was accepted by **ICSE 2025**! This is the first **CCF-A** SE conference paper in our group!


# 📝 Publications 

## Representative Works

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICSE 2025</div><img src='images/ICSE-25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Instruct or Interact? Exploring and Eliciting LLMs’ Capability in Code Snippet Adaptation Through Prompt Engineering](https://ieeexplore.ieee.org/document/11029912)


**Tanghaoran Zhang**, Yue Yu, Xinjun Mao, Shangwen Wang, Kang Yang, Yao Lu, Zhang Zhang and Yuxin Zhao.

**ICSE 2025** (<span style="color:red">CCF-A</span>)

[**Project**](https://github.com/ztwater/Instruct-or-Interact) 


- We first empirically investigate the capability of Large Language Models (LLMs) on the code adaptation task and find their sub-optimal performance are caused by three main reasons: (1) Unclear Requirement, (2) Requirement Misalignment and (3) Context Misapplication. To resolve above issues, we propose an interactive prompting approach to eliciting LLMs’ ability in code snippet adaptation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TSE 2024</div><img src='images/TSE-24.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">


[How Do Developers Adapt Code Snippets to Their Contexts? An Empirical Study of Context-Based Code Snippet Adaptations](https://ieeexplore.ieee.org/document/10510659)

**Tanghaoran Zhang**, Yao Lu, Yue Yu, Xinjun Mao, Yang Zhang and Yuxin Zhao.

**TSE 2024** (<span style="color:red">CCF-A</span>, SCI-Q1)

[**Project**](https://github.com/ztwater/how_to_adapt_code_snippet) 

- We investigate how developers adapt code snippets to their project context based on a semi-structured interview and a quantitative study on 300 real-world adaptation cases. We point out current challenges in the adaptation practices and obtain four typical context-based adaptation patterns. 
</div>
</div>

----

- [FENSE: A Feature-based Ensemble Modeling Approach to Cross-project Just-in-time Defect Prediction](https://link.springer.com/article/10.1007/s10664-022-10185-8), **Tanghaoran Zhang**, Yue Yu, Xinjun Mao, Yao Lu, Zhixing Li and Huaimin Wang, **EMSE** (CCF-B, JCR-Q1).

## All Publications
- [Understanding the Faults in Serverless Computing Based Applications: An Empirical Study](https://ztwater.github.io), Changrong Xie, Yang Zhang, Xinjun Mao, Kang Yang and **Tanghaoran Zhang**, **ICSME 2025** (CCF-B).

- [CARLDA: An Approach for Stack Overflow API Mention Recognition Driven by Context and LLM-based Data Augmentation](https://onlinelibrary.wiley.com/doi/10.1002/smr.70015), Zhang Zhang, Xinjun Mao, Shangwen Wang, Kang Yang, **Tanghaoran Zhang** and Yao Lu, **JSEP** (CCF-B).

- [Large Language Models are Qualified Benchmark Builders: Rebuilding Pre-Training Datasets for Advancing Code Intelligence Tasks](https://ieeexplore.ieee.org/document/11025927), Kang Yang, Xinjun Mao, Shangwen Wang, Yanlin Wang, **Tanghaoran Zhang**, Bo Lin, Yihao Qin, Zhang Zhang, Yao Lu and Kamal Al-Sabahi, **ICPC 2025** (CCF-B),  🏆 <span style="color:red">***ACM SIGSOFT Distinguished Paper Award***</span>.

- [Improving API Knowledge Comprehensibility: A Context-Dependent Entity Detection and Context Completion Approach Using LLM](https://ieeexplore.ieee.org/document/10992400), Zhang Zhang, Xinjun Mao, Shangwen Wang, Kang Yang, **Tanghaoran Zhang**, Fei Gao and Xunhui Zhang, **SANER 2025** (CCF-B).

- [An Empirical Study of Cross-Project Pull Request Recommendation in GitHub](), Wenyu Xu, Yao Lu, Xunhui Zhang, **Tanghaoran Zhang**, Bo Lin and Xinjun Mao, **APSEC 2024** (CCF-C).

- [MUSE: A Multi-Feature Semantic Fusion Method for ROS Node Search Based on Knowledge Graph](), Yuxin Zhao, Xinjun Mao, **Tanghaoran Zhang** and Zhang Zhang, **APSEC 2023** (CCF-C).

- [An Effective Method for Constructing Knowledge Graph to Search Reusable ROS Nodes](), Yuxin Zhao, Xinjun Mao, Sun Bo, **Tanghaoran Zhang** and Shuo Yang, **SEKE 2023** (CCF-C).

- [An Extensive Study of the Structure Features in Transformer-based Code Semantic Summarization](https://ieeexplore.ieee.org/document/10174079), Kang Yang, Xinjun Mao, Shangwen Wang, Yihao Qin, **Tanghaoran Zhang**, Yao Lu and Kamal Al-Sabahi, **ICPC 2023** (CCF-B).

- [Verifying ReLU Neural Networks from a Model Checking Perspective](https://link.springer.com/article/10.1007/s11390-020-0546-7), Wanwei Liu, Fu Song, **Tanghaoran Zhang** and Ji Wang, **JCST 2020** (CCF-B).

# 🎖 Honors and Awards
- *2025.04*, 🏆ACM SIGSOFT Distinguished Paper Award in ICPC 2025.
- *2023.03*, 💰Second-Prize Merit Scholarship, NUDT.
- *2020.05*, 💰Qiangjun Scholarship, NUDT.
- *2019.10*, 🏅Outstanding Winner of M* Modeling Contest.
- *2019.10*, 🏆CCF Outstanding Undergraduate, CCF.
- *2019.05*, 💰Yinhe Scholarship, College of Computer Science and Technology, NUDT.
- *2019.05*, 🏅Meritorious Winner of MCM/ICM.
- *2018.05*, 🏅Meritorious Winner of MCM/ICM.

# 📖 Educations
- *2020.09 - now*, National University of Defense Technology (NUDT), Ph.D. Student in Software Engineering. 
- *2016.09 - 2020.06*, Tsien Hsue-shen Class (**1/30**), National University of Defense Technology (NUDT), B.E. in Software Engineering. 
- *2010.09 - 2016.06*, The High School Affiliated to Renmin University of China (RDFZ), Middle and High School.

# ⚙️ Services
- **Reviewer**
  - EMSE, KAIS
- **External Reviewer**
  - Journal: TOSEM, JCST, JoS
  - Conference: ICLR'25, ASE'24, ESEM'24

# 💬 Invited Talks
- *2024.12*, ICSE 2025 Paper Pre-conference Presentation \| [Video](https://www.bilibili.com/video/BV1RhBjYgEJs).

# 💻 Internships
- *2025.03 - 2025.09*, Visiting student at Peng Cheng Laboratory, Shenzhen, Guangdong.
- *2019.07 - 2019.10*, Mitacs Research Internship, at [SEAL](https://seal-queensu.github.io) in Queen's University, Canada, supervised by Prof. Ying Zou.
