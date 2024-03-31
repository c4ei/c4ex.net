<template>
  <div class="main-top-wrapper">
    <div class="content">
      <div class="grid grid-cols-2 block1">
        <div class="block1-left">
          <h1>All About Health(AAH)</h1>
          <p class="block-text">
            <a class="btn2" href="https://docs.google.com/document/d/11h0WhWO0GCep63sKr9i0xM13nrllVVIBPZVs84re8Jk/edit?usp=sharing" target="_blank">싸이트 사용법</a> 
            <a class="btn2" href="https://c4ei.net" target="_blank">C4EI 홈페이지</a><br />
            <a class="btn2" href="https://shop.c4ei.net" target="_blank">AAH SHOP</a>
            <a class="btn2" href="https://docs.google.com/document/d/1yavY9OEqn0HUPwB_eUCxFQETealZdzQu1rj7yUnmV2M/edit?usp=sharing" target="_blank">AAH 구매법</a>
          </p>
          <div class="course">
            <img src="/img/btc.svg" class="inline-block" />
            <span>BTC Price: {{ course.toFixed(2) }} USDT</span>
          </div>
          <a class="btn" href="/account/trade/AAH-USDT">Trade AAH Now</a>
        </div>
        <div class="block1-right">
          <img src="/img/top.png" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ['course']
}
</script>
<style>
.main-top-wrapper {
  background: #292256;
  position: relative;
  padding: 157px 0 88px;
}
body h1 {
  color: #fff;
  padding-bottom: 29px;
  font-size: 60px;
  font-weight: 700;
  line-height: 64px;
}
.block-text {
  font-size: 24px;
  color: #FFF;
  padding-bottom: 29px;
}
.block1-left {
  padding-top: 100px;
}
.course {
  padding-bottom: 40px;
}
.course span {
  font-size: 18px;
  color: #fff;
  position: relative;
  left: 2px;
  top: 1px;
}
.btn2
{
    height: 42px;
    background: #6352CD;
    border-radius: 5px;
    font-weight: 400;
    color: #FFF;
    text-align: center;
    font-size: 16px;
    padding: 12px 5px 2px 5px;
    display: inline-block;
    margin-bottom: 2px;
}
@media(max-width: 900px) {
  .block1 {
    display: flex !important;
    flex-direction: column;
    align-items: center;
  }
  .block1-left {
    order: 1;
    padding-top: 36px;
  }
  .main-top-wrapper {
    padding: 62px 0 45px;
  }
  .block1-left h1 {
    padding-bottom: 12px;
    line-height: 1.4;
  }
  .block-text {
    font-size: 18px;
  }
  .course span {
    font-size: 16px;
  }
  .course {
    padding-bottom: 25px;
  }
  .btn {
    height: 44px;
    font-size: 13px;
    padding: 15px 30px;
    margin-bottom: 2px;
  }
}
</style>
