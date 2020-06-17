Capstone : DDOS 탐지 IDS + Django 모니터링 서비스
=====================================================================

## Setting
> 이 레포지토리를 git clone 해줍니다.
<pre><code>git clone [이 git repository 주소]</pre></code>
> setting & module install
<pre><code>cd 2020_Capstone_IDS</code></pre>
<pre><code>chmod 755 settinginstall.sh</code></pre>
<pre><code>./settinginstall.sh</code></pre>
------------------------------------------------------------------
## IDS 실행
> 1. Django 실행 
#### 새로운 터미널 창을 띄우고 진행합니다.
<pre><code>cd mysite</pre></code>
<pre><code>sudo python3 manage.py runserver</pre></code>

> 2. IDS 실행
#### 새로운 터미널 창을 띄우고 진행합니다.
<pre><code>cd ..</pre></code>
<pre><code>cd Capstone_DDOS_IDS</pre></code>
<pre><code>sudo python3 DDOS_IDS.py</pre></code>
