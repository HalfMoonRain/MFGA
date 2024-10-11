# 프로젝트 구조
frontend/
│
├── public/                      # 정적 파일을 포함 (index.html, 이미지, favicon 등)
│   ├── index.html               # HTML 템플릿
│   └── assets/                  # 이미지, 폰트, 아이콘 등의 정적 리소스
│
├── src/                         # 소스 파일이 위치하는 폴더
│   ├── api/                     # API 호출 관련 로직 (예: Axios)
│   │   ├── auth.js              # 인증 관련 API
│   │   ├── users.js             # 사용자 관련 API
│   │   └── index.js             # API 호출 모듈 진입점
│   │
│   ├── components/              # 재사용 가능한 UI 컴포넌트
│   │   ├── Button/              # 버튼 컴포넌트
│   │   │   ├── Button.jsx
│   │   │   ├── Button.css
│   │   │   └── index.js         # 컴포넌트의 엔트리 포인트
│   │   └── Header/              # 헤더 컴포넌트
│   │       ├── Header.jsx
│   │       ├── Header.css
│   │       └── index.js
│   │
│   ├── hooks/                   # 커스텀 훅 관리
│   │   ├── useAuth.js           # 인증 관련 커스텀 훅
│   │   ├── useFetch.js          # API 호출 관련 커스텀 훅
│   │   └── index.js
│   │
│   ├── pages/                   # 각 페이지별 컴포넌트
│   │   ├── Home/                # 홈 페이지
│   │   │   ├── Home.jsx
│   │   │   └── Home.css
│   │   ├── Login/               # 로그인 페이지
│   │   │   ├── Login.jsx
│   │   │   └── Login.css
│   │   └── Dashboard/           # 대시보드 페이지
│   │       ├── Dashboard.jsx
│   │       └── Dashboard.css
│   │
│   ├── services/                # 비즈니스 로직 관리
│   │   ├── authService.js       # 인증 서비스
│   │   ├── userService.js       # 사용자 서비스
│   │   └── index.js
│   │
│   ├── store/                   # 상태 관리 (예: Redux 또는 Context API)
│   │   ├── slices/              # Redux 슬라이스
│   │   │   ├── authSlice.js     # 인증 상태 관리
│   │   │   └── userSlice.js     # 사용자 상태 관리
│   │   ├── store.js             # Redux 스토어 설정
│   │   └── index.js
│   │
│   ├── styles/                  # 전역 스타일 관리
│   │   ├── global.css           # 전역 CSS
│   │   └── variables.css        # CSS 변수 (색상, 폰트 등)
│   │
│   ├── utils/                   # 유틸리티 함수 모음
│   │   ├── helpers.js           # 헬퍼 함수
│   │   ├── validators.js        # 입력 검증 함수
│   │   └── index.js
│   │
│   ├── App.jsx                  # 최상위 React 컴포넌트
│   ├── index.js                 # ReactDOM 진입점
│   └── setupTests.js            # 테스트 환경 설정
│
├── .env                         # 환경 변수 설정 파일
├── package.json                 # 프로젝트 의존성 관리
├── webpack.config.js            # Webpack 설정 파일 (필요 시)
└── README.md                    # 프로젝트 설명

## 설명
 - public: 정적 파일을 저장하는 곳으로, index.html 파일과 정적 리소스들이 위치합니다.
 - src: 실제 소스 코드가 있는 폴더입니다.
 - api: 서버와 통신하는 API 호출 로직을 모듈화하여 관리합니다.
 - components: 재사용 가능한 UI 컴포넌트들을 관리합니다. 각 컴포넌트는 해당 컴포넌트만의 폴더를 가지고 있으며, JSX, CSS, 필요한 파일들을 모두 포함합니다.
 - hooks: 커스텀 훅을 정의하여 상태 관리나 비즈니스 로직을 재사용할 수 있습니다.
 - pages: 페이지별로 컴포넌트를 관리하여, 라우팅에 사용할 수 있는 컴포넌트들입니다.
 - services: 비즈니스 로직을 처리하는 서비스들을 모아두는 폴더입니다. 여기서 비즈니스 로직과 컴포넌트의 결합을 최소화할 수 있습니다.
 - store: 전역 상태 관리 (예: Redux)와 관련된 파일들을 포함합니다.
 - styles: 전역 CSS 파일 및 공통 스타일 변수를 관리합니다.
 - utils: 프로젝트 내에서 자주 사용하는 유틸리티 함수들을 모아두는 곳입니다.
 - App.jsx: React 애플리케이션의 최상위 컴포넌트입니다.
 - index.js: ReactDOM을 통해 최상위 컴포넌트를 HTML에 렌더링하는 진입점입니다.
 - setupTests.js: 테스트를 위한 설정 파일로, Jest와 같은 도구를 설정할 때 사용됩니다.
## 추가 설명
    프로젝트의 규모와 요구 사항에 따라 상태 관리를 위한 도구 (예: Redux, Context API)를 선택할 수 있습니다.
    Webpack, Babel 등 빌드 도구의 설정이 필요할 경우 webpack.config.js 파일을 추가하여 관리합니다.
    각 컴포넌트와 페이지는 자신만의 스타일 파일을 가지고 있어, 스타일이 서로 겹치지 않도록 관리할 수 있습니다.