/*! For license information please see 612.7ca668d53625da2603a7.js.LICENSE.txt */
"use strict";(self.webpackChunk_epi2melabs_epi2melabs_wfpage=self.webpackChunk_epi2melabs_epi2melabs_wfpage||[]).push([[612],{2122:(e,t,n)=>{function a(){return a=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e},a.apply(this,arguments)}n.d(t,{Z:()=>a})},7612:(e,t,n)=>{n.r(t),n.d(t,{BrowserRouter:()=>re,HashRouter:()=>ie,Link:()=>ue,MemoryRouter:()=>K,NavLink:()=>le,Navigate:()=>V,NavigationType:()=>a,Outlet:()=>q,Route:()=>z,Router:()=>G,Routes:()=>Q,UNSAFE_LocationContext:()=>d,UNSAFE_NavigationContext:()=>v,UNSAFE_RouteContext:()=>m,createPath:()=>f,createRoutesFromChildren:()=>X,createSearchParams:()=>he,generatePath:()=>y,matchPath:()=>C,matchRoutes:()=>b,parsePath:()=>p,renderMatches:()=>Y,resolvePath:()=>S,unstable_HistoryRouter:()=>oe,useHref:()=>$,useInRouterContext:()=>j,useLinkClickHandler:()=>ce,useLocation:()=>B,useMatch:()=>_,useNavigate:()=>H,useNavigationType:()=>W,useOutlet:()=>U,useOutletContext:()=>I,useParams:()=>Z,useResolvedPath:()=>F,useRoutes:()=>D,useSearchParams:()=>se});var a,r=n(6271),i=n(2122);!function(e){e.Pop="POP",e.Push="PUSH",e.Replace="REPLACE"}(a||(a={}));var o="beforeunload",u="popstate";function l(e,t,n){return Math.min(Math.max(e,t),n)}function c(e){e.preventDefault(),e.returnValue=""}function s(){var e=[];return{get length(){return e.length},push:function(t){return e.push(t),function(){e=e.filter((function(e){return e!==t}))}},call:function(t){e.forEach((function(e){return e&&e(t)}))}}}function h(){return Math.random().toString(36).substr(2,8)}function f(e){var t=e.pathname,n=void 0===t?"/":t,a=e.search,r=void 0===a?"":a,i=e.hash,o=void 0===i?"":i;return r&&"?"!==r&&(n+="?"===r.charAt(0)?r:"?"+r),o&&"#"!==o&&(n+="#"===o.charAt(0)?o:"#"+o),n}function p(e){var t={};if(e){var n=e.indexOf("#");n>=0&&(t.hash=e.substr(n),e=e.substr(0,n));var a=e.indexOf("?");a>=0&&(t.search=e.substr(a),e=e.substr(0,a)),e&&(t.pathname=e)}return t}const v=(0,r.createContext)(null),d=(0,r.createContext)(null),m=(0,r.createContext)({outlet:null,matches:[]});function g(e,t){if(!e)throw new Error(t)}function y(e,t){return void 0===t&&(t={}),e.replace(/:(\w+)/g,((e,n)=>(null==t[n]&&g(!1),t[n]))).replace(/\/*\*$/,(e=>null==t["*"]?"":t["*"].replace(/^\/*/,"/")))}function b(e,t,n){void 0===n&&(n="/");let a=O(("string"==typeof t?p(t):t).pathname||"/",n);if(null==a)return null;let r=x(e);!function(e){e.sort(((e,t)=>e.score!==t.score?t.score-e.score:function(e,t){return e.length===t.length&&e.slice(0,-1).every(((e,n)=>e===t[n]))?e[e.length-1]-t[t.length-1]:0}(e.routesMeta.map((e=>e.childrenIndex)),t.routesMeta.map((e=>e.childrenIndex)))))}(r);let i=null;for(let e=0;null==i&&e<r.length;++e)i=w(r[e],a);return i}function x(e,t,n,a){return void 0===t&&(t=[]),void 0===n&&(n=[]),void 0===a&&(a=""),e.forEach(((e,r)=>{let i={relativePath:e.path||"",caseSensitive:!0===e.caseSensitive,childrenIndex:r,route:e};i.relativePath.startsWith("/")&&(i.relativePath.startsWith(a)||g(!1),i.relativePath=i.relativePath.slice(a.length));let o=L([a,i.relativePath]),u=n.concat(i);e.children&&e.children.length>0&&(!0===e.index&&g(!1),x(e.children,t,u,o)),(null!=e.path||e.index)&&t.push({path:o,score:k(o,e.index),routesMeta:u})})),t}const P=/^:\w+$/,E=e=>"*"===e;function k(e,t){let n=e.split("/"),a=n.length;return n.some(E)&&(a+=-2),t&&(a+=2),n.filter((e=>!E(e))).reduce(((e,t)=>e+(P.test(t)?3:""===t?1:10)),a)}function w(e,t){let{routesMeta:n}=e,a={},r="/",i=[];for(let e=0;e<n.length;++e){let o=n[e],u=e===n.length-1,l="/"===r?t:t.slice(r.length)||"/",c=C({path:o.relativePath,caseSensitive:o.caseSensitive,end:u},l);if(!c)return null;Object.assign(a,c.params);let s=o.route;i.push({params:a,pathname:L([r,c.pathname]),pathnameBase:A(L([r,c.pathnameBase])),route:s}),"/"!==c.pathnameBase&&(r=L([r,c.pathnameBase]))}return i}function C(e,t){"string"==typeof e&&(e={path:e,caseSensitive:!1,end:!0});let[n,a]=function(e,t,n){void 0===t&&(t=!1),void 0===n&&(n=!0);let a=[],r="^"+e.replace(/\/*\*?$/,"").replace(/^\/*/,"/").replace(/[\\.*+^$?{}|()[\]]/g,"\\$&").replace(/:(\w+)/g,((e,t)=>(a.push(t),"([^\\/]+)")));return e.endsWith("*")?(a.push("*"),r+="*"===e||"/*"===e?"(.*)$":"(?:\\/(.+)|\\/*)$"):r+=n?"\\/*$":"(?:(?=[.~-]|%[0-9A-F]{2})|\\b|\\/|$)",[new RegExp(r,t?void 0:"i"),a]}(e.path,e.caseSensitive,e.end),r=t.match(n);if(!r)return null;let i=r[0],o=i.replace(/(.)\/+$/,"$1"),u=r.slice(1);return{params:a.reduce(((e,t,n)=>{if("*"===t){let e=u[n]||"";o=i.slice(0,i.length-e.length).replace(/(.)\/+$/,"$1")}return e[t]=function(e,t){try{return decodeURIComponent(e)}catch(t){return e}}(u[n]||""),e}),{}),pathname:i,pathnameBase:o,pattern:e}}function S(e,t){void 0===t&&(t="/");let{pathname:n,search:a="",hash:r=""}="string"==typeof e?p(e):e,i=n?n.startsWith("/")?n:function(e,t){let n=t.replace(/\/+$/,"").split("/");return e.split("/").forEach((e=>{".."===e?n.length>1&&n.pop():"."!==e&&n.push(e)})),n.length>1?n.join("/"):"/"}(n,t):t;return{pathname:i,search:N(a),hash:M(r)}}function R(e,t,n){let a,r="string"==typeof e?p(e):e,i=""===e||""===r.pathname?"/":r.pathname;if(null==i)a=n;else{let e=t.length-1;if(i.startsWith("..")){let t=i.split("/");for(;".."===t[0];)t.shift(),e-=1;r.pathname=t.join("/")}a=e>=0?t[e]:"/"}let o=S(r,a);return i&&"/"!==i&&i.endsWith("/")&&!o.pathname.endsWith("/")&&(o.pathname+="/"),o}function O(e,t){if("/"===t)return e;if(!e.toLowerCase().startsWith(t.toLowerCase()))return null;let n=e.charAt(t.length);return n&&"/"!==n?null:e.slice(t.length)||"/"}const L=e=>e.join("/").replace(/\/\/+/g,"/"),A=e=>e.replace(/\/+$/,"").replace(/^\/*/,"/"),N=e=>e&&"?"!==e?e.startsWith("?")?e:"?"+e:"",M=e=>e&&"#"!==e?e.startsWith("#")?e:"#"+e:"";function $(e){j()||g(!1);let{basename:t,navigator:n}=(0,r.useContext)(v),{hash:a,pathname:i,search:o}=F(e),u=i;if("/"!==t){let n=function(e){return""===e||""===e.pathname?"/":"string"==typeof e?p(e).pathname:e.pathname}(e),a=null!=n&&n.endsWith("/");u="/"===i?t+(a?"/":""):L([t,i])}return n.createHref({pathname:u,search:o,hash:a})}function j(){return null!=(0,r.useContext)(d)}function B(){return j()||g(!1),(0,r.useContext)(d).location}function W(){return(0,r.useContext)(d).navigationType}function _(e){j()||g(!1);let{pathname:t}=B();return(0,r.useMemo)((()=>C(e,t)),[t,e])}function H(){j()||g(!1);let{basename:e,navigator:t}=(0,r.useContext)(v),{matches:n}=(0,r.useContext)(m),{pathname:a}=B(),i=JSON.stringify(n.map((e=>e.pathnameBase))),o=(0,r.useRef)(!1);return(0,r.useEffect)((()=>{o.current=!0})),(0,r.useCallback)((function(n,r){if(void 0===r&&(r={}),!o.current)return;if("number"==typeof n)return void t.go(n);let u=R(n,JSON.parse(i),a);"/"!==e&&(u.pathname=L([e,u.pathname])),(r.replace?t.replace:t.push)(u,r.state)}),[e,t,i,a])}const T=(0,r.createContext)(null);function I(){return(0,r.useContext)(T)}function U(e){let t=(0,r.useContext)(m).outlet;return t?(0,r.createElement)(T.Provider,{value:e},t):t}function Z(){let{matches:e}=(0,r.useContext)(m),t=e[e.length-1];return t?t.params:{}}function F(e){let{matches:t}=(0,r.useContext)(m),{pathname:n}=B(),a=JSON.stringify(t.map((e=>e.pathnameBase)));return(0,r.useMemo)((()=>R(e,JSON.parse(a),n)),[e,a,n])}function D(e,t){j()||g(!1);let{matches:n}=(0,r.useContext)(m),a=n[n.length-1],i=a?a.params:{},o=(a&&a.pathname,a?a.pathnameBase:"/");a&&a.route;let u,l=B();if(t){var c;let e="string"==typeof t?p(t):t;"/"===o||(null==(c=e.pathname)?void 0:c.startsWith(o))||g(!1),u=e}else u=l;let s=u.pathname||"/",h=b(e,{pathname:"/"===o?s:s.slice(o.length)||"/"});return J(h&&h.map((e=>Object.assign({},e,{params:Object.assign({},i,e.params),pathname:L([o,e.pathname]),pathnameBase:"/"===e.pathnameBase?o:L([o,e.pathnameBase])}))),n)}function J(e,t){return void 0===t&&(t=[]),null==e?null:e.reduceRight(((n,a,i)=>(0,r.createElement)(m.Provider,{children:void 0!==a.route.element?a.route.element:n,value:{outlet:n,matches:t.concat(e.slice(0,i+1))}})),null)}function K(e){let{basename:t,children:n,initialEntries:o,initialIndex:u}=e,c=(0,r.useRef)();null==c.current&&(c.current=function(e){void 0===e&&(e={});var t=e,n=t.initialEntries,r=void 0===n?["/"]:n,o=t.initialIndex,u=r.map((function(e){return(0,i.Z)({pathname:"/",search:"",hash:"",state:null,key:h()},"string"==typeof e?p(e):e)})),c=l(null==o?u.length-1:o,0,u.length-1),v=a.Pop,d=u[c],m=s(),g=s();function y(e,t){return void 0===t&&(t=null),(0,i.Z)({pathname:d.pathname,search:"",hash:""},"string"==typeof e?p(e):e,{state:t,key:h()})}function b(e,t,n){return!g.length||(g.call({action:e,location:t,retry:n}),!1)}function x(e,t){v=e,d=t,m.call({action:v,location:d})}function P(e){var t=l(c+e,0,u.length-1),n=a.Pop,r=u[t];b(n,r,(function(){P(e)}))&&(c=t,x(n,r))}var E={get index(){return c},get action(){return v},get location(){return d},createHref:function(e){return"string"==typeof e?e:f(e)},push:function e(t,n){var r=a.Push,i=y(t,n);b(r,i,(function(){e(t,n)}))&&(c+=1,u.splice(c,u.length,i),x(r,i))},replace:function e(t,n){var r=a.Replace,i=y(t,n);b(r,i,(function(){e(t,n)}))&&(u[c]=i,x(r,i))},go:P,back:function(){P(-1)},forward:function(){P(1)},listen:function(e){return m.push(e)},block:function(e){return g.push(e)}};return E}({initialEntries:o,initialIndex:u}));let v=c.current,[d,m]=(0,r.useState)({action:v.action,location:v.location});return(0,r.useLayoutEffect)((()=>v.listen(m)),[v]),(0,r.createElement)(G,{basename:t,children:n,location:d.location,navigationType:d.action,navigator:v})}function V(e){let{to:t,replace:n,state:a}=e;j()||g(!1);let i=H();return(0,r.useEffect)((()=>{i(t,{replace:n,state:a})})),null}function q(e){return U(e.context)}function z(e){g(!1)}function G(e){let{basename:t="/",children:n=null,location:i,navigationType:o=a.Pop,navigator:u,static:l=!1}=e;j()&&g(!1);let c=A(t),s=(0,r.useMemo)((()=>({basename:c,navigator:u,static:l})),[c,u,l]);"string"==typeof i&&(i=p(i));let{pathname:h="/",search:f="",hash:m="",state:y=null,key:b="default"}=i,x=(0,r.useMemo)((()=>{let e=O(h,c);return null==e?null:{pathname:e,search:f,hash:m,state:y,key:b}}),[c,h,f,m,y,b]);return null==x?null:(0,r.createElement)(v.Provider,{value:s},(0,r.createElement)(d.Provider,{children:n,value:{location:x,navigationType:o}}))}function Q(e){let{children:t,location:n}=e;return D(X(t),n)}function X(e){let t=[];return r.Children.forEach(e,(e=>{if(!(0,r.isValidElement)(e))return;if(e.type===r.Fragment)return void t.push.apply(t,X(e.props.children));e.type!==z&&g(!1);let n={caseSensitive:e.props.caseSensitive,element:e.props.element,index:e.props.index,path:e.props.path};e.props.children&&(n.children=X(e.props.children)),t.push(n)})),t}function Y(e){return J(e)}function ee(){return ee=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e},ee.apply(this,arguments)}function te(e,t){if(null==e)return{};var n,a,r={},i=Object.keys(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}const ne=["onClick","reloadDocument","replace","state","target","to"],ae=["aria-current","caseSensitive","className","end","style","to","children"];function re(e){let{basename:t,children:n,window:l}=e,v=(0,r.useRef)();null==v.current&&(v.current=function(e){void 0===e&&(e={});var t=e.window,n=void 0===t?document.defaultView:t,r=n.history;function l(){var e=n.location,t=e.pathname,a=e.search,i=e.hash,o=r.state||{};return[o.idx,{pathname:t,search:a,hash:i,state:o.usr||null,key:o.key||"default"}]}var v=null;n.addEventListener(u,(function(){if(v)x.call(v),v=null;else{var e=a.Pop,t=l(),n=t[0],r=t[1];if(x.length){if(null!=n){var i=g-n;i&&(v={action:e,location:r,retry:function(){S(-1*i)}},S(i))}}else C(e)}}));var d=a.Pop,m=l(),g=m[0],y=m[1],b=s(),x=s();function P(e){return"string"==typeof e?e:f(e)}function E(e,t){return void 0===t&&(t=null),(0,i.Z)({pathname:y.pathname,hash:"",search:""},"string"==typeof e?p(e):e,{state:t,key:h()})}function k(e,t){return[{usr:e.state,key:e.key,idx:t},P(e)]}function w(e,t,n){return!x.length||(x.call({action:e,location:t,retry:n}),!1)}function C(e){d=e;var t=l();g=t[0],y=t[1],b.call({action:d,location:y})}function S(e){r.go(e)}null==g&&(g=0,r.replaceState((0,i.Z)({},r.state,{idx:g}),""));var R={get action(){return d},get location(){return y},createHref:P,push:function e(t,i){var o=a.Push,u=E(t,i);if(w(o,u,(function(){e(t,i)}))){var l=k(u,g+1),c=l[0],s=l[1];try{r.pushState(c,"",s)}catch(e){n.location.assign(s)}C(o)}},replace:function e(t,n){var i=a.Replace,o=E(t,n);if(w(i,o,(function(){e(t,n)}))){var u=k(o,g),l=u[0],c=u[1];r.replaceState(l,"",c),C(i)}},go:S,back:function(){S(-1)},forward:function(){S(1)},listen:function(e){return b.push(e)},block:function(e){var t=x.push(e);return 1===x.length&&n.addEventListener(o,c),function(){t(),x.length||n.removeEventListener(o,c)}}};return R}({window:l}));let d=v.current,[m,g]=(0,r.useState)({action:d.action,location:d.location});return(0,r.useLayoutEffect)((()=>d.listen(g)),[d]),(0,r.createElement)(G,{basename:t,children:n,location:m.location,navigationType:m.action,navigator:d})}function ie(e){let{basename:t,children:n,window:l}=e,v=(0,r.useRef)();null==v.current&&(v.current=function(e){void 0===e&&(e={});var t=e.window,n=void 0===t?document.defaultView:t,r=n.history;function l(){var e=p(n.location.hash.substr(1)),t=e.pathname,a=void 0===t?"/":t,i=e.search,o=void 0===i?"":i,u=e.hash,l=void 0===u?"":u,c=r.state||{};return[c.idx,{pathname:a,search:o,hash:l,state:c.usr||null,key:c.key||"default"}]}var v=null;function d(){if(v)P.call(v),v=null;else{var e=a.Pop,t=l(),n=t[0],r=t[1];if(P.length){if(null!=n){var i=y-n;i&&(v={action:e,location:r,retry:function(){R(-1*i)}},R(i))}}else S(e)}}n.addEventListener(u,d),n.addEventListener("hashchange",(function(){f(l()[1])!==f(b)&&d()}));var m=a.Pop,g=l(),y=g[0],b=g[1],x=s(),P=s();function E(e){return function(){var e=document.querySelector("base"),t="";if(e&&e.getAttribute("href")){var a=n.location.href,r=a.indexOf("#");t=-1===r?a:a.slice(0,r)}return t}()+"#"+("string"==typeof e?e:f(e))}function k(e,t){return void 0===t&&(t=null),(0,i.Z)({pathname:b.pathname,hash:"",search:""},"string"==typeof e?p(e):e,{state:t,key:h()})}function w(e,t){return[{usr:e.state,key:e.key,idx:t},E(e)]}function C(e,t,n){return!P.length||(P.call({action:e,location:t,retry:n}),!1)}function S(e){m=e;var t=l();y=t[0],b=t[1],x.call({action:m,location:b})}function R(e){r.go(e)}return null==y&&(y=0,r.replaceState((0,i.Z)({},r.state,{idx:y}),"")),{get action(){return m},get location(){return b},createHref:E,push:function e(t,i){var o=a.Push,u=k(t,i);if(C(o,u,(function(){e(t,i)}))){var l=w(u,y+1),c=l[0],s=l[1];try{r.pushState(c,"",s)}catch(e){n.location.assign(s)}S(o)}},replace:function e(t,n){var i=a.Replace,o=k(t,n);if(C(i,o,(function(){e(t,n)}))){var u=w(o,y),l=u[0],c=u[1];r.replaceState(l,"",c),S(i)}},go:R,back:function(){R(-1)},forward:function(){R(1)},listen:function(e){return x.push(e)},block:function(e){var t=P.push(e);return 1===P.length&&n.addEventListener(o,c),function(){t(),P.length||n.removeEventListener(o,c)}}}}({window:l}));let d=v.current,[m,g]=(0,r.useState)({action:d.action,location:d.location});return(0,r.useLayoutEffect)((()=>d.listen(g)),[d]),(0,r.createElement)(G,{basename:t,children:n,location:m.location,navigationType:m.action,navigator:d})}function oe(e){let{basename:t,children:n,history:a}=e;const[i,o]=(0,r.useState)({action:a.action,location:a.location});return(0,r.useLayoutEffect)((()=>a.listen(o)),[a]),(0,r.createElement)(G,{basename:t,children:n,location:i.location,navigationType:i.action,navigator:a})}const ue=(0,r.forwardRef)((function(e,t){let{onClick:n,reloadDocument:a,replace:i=!1,state:o,target:u,to:l}=e,c=te(e,ne),s=$(l),h=ce(l,{replace:i,state:o,target:u});return(0,r.createElement)("a",ee({},c,{href:s,onClick:function(e){n&&n(e),e.defaultPrevented||a||h(e)},ref:t,target:u}))})),le=(0,r.forwardRef)((function(e,t){let{"aria-current":n="page",caseSensitive:a=!1,className:i="",end:o=!1,style:u,to:l,children:c}=e,s=te(e,ae),h=B(),f=F(l),p=h.pathname,v=f.pathname;a||(p=p.toLowerCase(),v=v.toLowerCase());let d,m=p===v||!o&&p.startsWith(v)&&"/"===p.charAt(v.length),g=m?n:void 0;d="function"==typeof i?i({isActive:m}):[i,m?"active":null].filter(Boolean).join(" ");let y="function"==typeof u?u({isActive:m}):u;return(0,r.createElement)(ue,ee({},s,{"aria-current":g,className:d,ref:t,style:y,to:l}),"function"==typeof c?c({isActive:m}):c)}));function ce(e,t){let{target:n,replace:a,state:i}=void 0===t?{}:t,o=H(),u=B(),l=F(e);return(0,r.useCallback)((t=>{if(!(0!==t.button||n&&"_self"!==n||function(e){return!!(e.metaKey||e.altKey||e.ctrlKey||e.shiftKey)}(t))){t.preventDefault();let n=!!a||f(u)===f(l);o(e,{replace:n,state:i})}}),[u,o,l,a,i,n,e])}function se(e){let t=(0,r.useRef)(he(e)),n=B(),a=(0,r.useMemo)((()=>{let e=he(n.search);for(let n of t.current.keys())e.has(n)||t.current.getAll(n).forEach((t=>{e.append(n,t)}));return e}),[n.search]),i=H();return[a,(0,r.useCallback)(((e,t)=>{i("?"+he(e),t)}),[i])]}function he(e){return void 0===e&&(e=""),new URLSearchParams("string"==typeof e||Array.isArray(e)||e instanceof URLSearchParams?e:Object.keys(e).reduce(((t,n)=>{let a=e[n];return t.concat(Array.isArray(a)?a.map((e=>[n,e])):[[n,a]])}),[]))}}}]);