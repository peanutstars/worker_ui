## venv

### Python 가상 환경 생성: 
```
#> python3 -m venv venv
```


## tailwindcss

### Troubleshoot
#### @apply 이슈
html 내의 <style></style> 안에서 @apply가 적용되지 않는 현상

| Before | After |
|--------|-------|
| `<style>...</style>` | `<style type="text/tailwindcss">...</style>` |



### 참조 사이트  
+ https://stackoverflow.com/questions/76288651/how-can-use-apply-directive-with-tailwindcss-cdn
+ https://flowbite.com/docs/getting-started/flask/
+ https://tailwindcss.com/docs/installation/tailwind-cli