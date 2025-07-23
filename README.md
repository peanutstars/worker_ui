## venv

### Python 가상 환경 생성: 
```
#> python3 -m venv venv
```


## tailwindcss

### install

+ Step #1
    ```
    sudo apt purge nodejs npm -y
    sudo rm -rf /etc/apt/sources.list.d/nodesource.list # If you added NodeSource repo
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
    ```

+ Step #2
  + 터미널 새로 열기

+ Step #3
    ```
    nvm install --lts
    nvm use --lts
    cd my_project || mkdir my_project
    rm -rf node_modules package-lock.json
    npm install tailwindcss @tailwindcss/cli
    ```

### build
```
npx @tailwindcss/cli -i ./src/static/css/input.css -o ./src/static/css/output.css
```

### input.css
```
@import "tailwindcss";

/* 기본 폰트 설정 */
body {
    font-family: 'Noto Sans KR', 'Inter', sans-serif;
    overscroll-behavior: none; /* 터치 스크롤 시 페이지 전체가 움직이는 현상 방지 */
}
/* 사이드바 축소 시 텍스트 숨김 */
.sidebar-collapsed .menu-text {
    display: none;
}
/* 사이드바 축소 시 아이콘 가운데 정렬 */
.sidebar-collapsed .menu-item {
    justify-content: center;
}
/* 스크롤바 디자인 */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: #f1f5f9;
}
::-webkit-scrollbar-thumb {
    background: #94a3b8;
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: #64748b;
}
/* 활성 메뉴 스타일 */
.menu-active {
    background-color: #2563eb; /* bg-blue-600 */
    color: white;
}
/* 비활성 메뉴 스타일 */
.menu-inactive {
    color: #cbd5e1; /* text-slate-300 */
}
.menu-inactive:hover {
    background-color: #334155; /* hover:bg-slate-700 */
}
/* 키패드/키보드 버튼 스타일 */
.keypad-btn, .keyboard-btn {
    @apply h-12 bg-slate-200 rounded-md text-lg font-semibold text-slate-700 flex items-center justify-center transition-colors hover:bg-slate-300 border border-slate-300;
}
.keyboard-btn.active {
    @apply bg-blue-500 text-white;
}
```

### Troubleshoot

#### bg-opacity issue

+ 빌드 진행한 output.css 를 사용하면, 내부에 bg-opacity-xxx 클래스가 정의가 없다.
+ 임시 해결 방법
    + script와 output.css 둘다 사용
    ```
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{{url_for('static',filename='css/output.css')}}">
    ```



### 참조 사이트  
+ https://flowbite.com/docs/getting-started/flask/
+ https://tailwindcss.com/docs/installation/tailwind-cli