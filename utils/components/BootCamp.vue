<template>
  <div id="BootCamp">

    <header1></header1>
    <div class="bootcamp-description layout-no-margin-top">
      <div>
        <h1>与心仪的课程偶遇</h1>
        <!--        <h4>资深工程师指导学习，实战中融会贯通IT技术</h4>-->
      </div>
    </div>

    <div class="bootcamp-features">
      <div class="container">
        <div class="row">
          <div class="col-md-3">
            <img src="../../static/img/bootcamp-project.png">
            <div class="bootcamp-features-description">
              <span>优秀项目</span>
              <span>专注实战</span>
            </div>
          </div>
          <div class="col-md-3">
            <img style=" padding-left: 24px;" src="../../static/img/bootcamp-teacher.png">
            <div class="bootcamp-features-description">
              <span>技术大牛</span>
              <span>有问必答</span>
            </div>
          </div>
          <div class="col-md-3">
            <img src="../../static/img/bootcamp-comment.png">
            <div class="bootcamp-features-description">
              <span>实验报告</span>
              <span>悉心点评</span>
            </div>
          </div>
          <div class="col-md-3">
            <img src="../../static/img/bootcamp-certificate.png">
            <div class="bootcamp-features-description">
              <span>完成课程</span>
              <span>获得证书</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="bootcamp-courses">
      <div class="container">
        <div class="bootcamp-courses-header">
          <h4 class="bootcamp-courses-title">秒杀课程</h4>
        </div>

        <div class="bootcamp-courses-body">

          <div class="media bootcamp-courses-item" v-for="(i,index) in courses" :key="index"
               v-show="new Date()<new Date(i.date+' '+i.end)">
            <div class="pull-right bootcamp-courses-order">

              <div class="pull-left">
                <span style="margin-bottom: -8px;">活动时限: {{i.start}}--{{i.end}}</span>
                <br>
                <h3>活动名称:{{i.act_name}}</h3>
                <h3 v-if="new Date(i.date+' '+i.start)>new Date()">倒计时:{{i.update_time}}</h3>
                <h3 v-if="new Date(i.date+' '+i.start)<new Date() &&new Date()<new Date(i.date+' '+i.end)">抢购中</h3>
                <h5>剩余 {{i.count}} 个课程</h5>
              </div>

            </div>
            <div class="course-img">
              <img class="media-object" :src="i.pic" height="300px" width="500">
            </div>
            <div class="media-body bootcamp-courses-body">
              <div class="bootcamp-courses-info">

                <h1>课程名称:{{i.course_name}}</h1>
                <div><p>课程信息: {{i.info}}</p></div>
                <!--<div>推荐先学：<a href="https://www.shiyanlou.com/courses/1" target="_blank">Linux基础入门</a> </div>-->
                <div>
                  <!--                  <p><a class="tagStyle2">Kali</a><a class="tagStyle2">渗透测试</a><a clas````````````````````````````\\2">Linux</a></p>-->
                </div>
              </div>
              <div class="bootcamp-courses-subscribe">
                <div class="pull-right bootcamp-courses-order">

                  <div class="pull-left">
                    <span style="margin-bottom: -8px;">￥{{i.sk_price}}</span>
                  </div>
                  <!--                  <a class="btn pull-right disabled" href="../courses/show2.html">秒杀</a>-->
                  <a
                    :class="{btn:true,'pull-right':true ,disabled:new Date(i.date+' '+i.start)>new Date() || new Date(i.date+' '+i.end)<new Date()}"
                    href="#" @click="sk(i)" v-if="user_id !=undefined">秒杀</a>
                  <a v-else class="btn pull-right" href="javascript:;">登录后参与秒杀</a>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
    <!--    <div class="bootcamp-faq">-->
    <!--      <div class="container">-->
    <!--        <div class="bootcamp-faq-header">-->
    <!--          <h4 class="bootcamp-faq-title">训练营FAQ</h4>-->
    <!--        </div>-->
    <!--        <div class="bootcamp-faq-body">-->
    <!--          <div class="bootcamp-faq-question">-->
    <!--            WHAT：实验楼训练营是什么？-->
    <!--          </div>-->
    <!--          <div class="bootcamp-faq-answer">-->
    <!--            <img src="../../static/img/bootcamp-answer.png">：训练营是一系列有教师服务（有问必答，实验报告点评等）的实验课。您将在教师指导下，在实验楼中完成一个可上线运行的产品原型或一系列编程任务，项目实战中融会贯通2-3门IT技术及开发流程。-->
    <!--          </div>-->
    <!--          <div class="bootcamp-faq-question">-->
    <!--            WHY：为什么选择实验楼训练营课程？-->
    <!--          </div>-->
    <!--          <div class="bootcamp-faq-answer">-->
    <!--            <img src="../../static/img/bootcamp-answer.png">：实战，实战，实战！课程教师是具备多年研发经验的资深工程师，课程选题来自优秀的开源技术或仿知名网站。非常适合已学基础技术却迷茫不知道如何运用的同学，零基础的同学可按课程要求学习推荐的先学课程。-->
    <!--          </div>-->
    <!--          <div class="bootcamp-faq-question">-->
    <!--            HOW：训练营课程学习流程是怎样的？-->
    <!--          </div>-->
    <!--          <div class="bootcamp-faq-answer">-->
    <!--            <img src="../../static/img/bootcamp-answer.png">：按实验文档依次完成实验，公开实验报告，实验中的问题随时在问答中提交，教师24小时内回复问答。完成所有实验并认真提交实验报告，可获得GOOD或PASS课程证书。-->
    <!--          </div>-->
    <!--        </div>-->
    <!--        <div class="bootcamp-faq-footer">-->
    <!--          <a class="bootcamp-faq-more" href="/questions/918" target="_blank">更多疑问，查看这里>></a>-->
    <!--        </div>-->
    <!--      </div>-->
    <!--    </div>-->


    <div class="modal fade" id="invite-user" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span
              class="sr-only">Close</span></button>
            <h4 class="modal-title">邀请好友，双方都可获赠实验豆！</h4>
          </div>
          <div class="modal-body">

            <div><h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！</h4>
            </div>

            <div id="msg-modal"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="flash-message" tabindex="-1" role="dialog">
      <div class="modal-dialog" rolw="document">
        <h1>订单生产中,将跳转至支付页面</h1>
      </div>
    </div>
    <div class="modal fade" id="modal-message" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span
              class="sr-only">Close</span></button>
            <h4 class="modal-title">注意</h4>
          </div>
          <div class="modal-body">
            <h4>商品名称:{{buyWhat.course_name}}</h4>
            <h5>价格:{{buyWhat.sk_price}}</h5>
            秒杀课程无法使用积分优惠券,将使用以下支付方式,继续交易请按确定
            <br>
            <input type="radio" checked>
            <img src="../../static/img/Snipaste_2019-10-17_10-29-45.png" style="height: 50px;width: 150px">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary confirm" data-dismiss="modal" @click="buy(buyWhat)">确定
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="sign-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
          <button type="button" class="close-modal" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span>
          </button>
          <div class="modal-body">
            <ul class="nav nav-tabs" role="tablist">
              <li role="presentation" class="active">
                <a href="#signin-form" aria-controls="signin-form" role="tab" data-toggle="tab">登录</a>
              </li>
              <li role="presentation">
                <a href="#signup-form" aria-controls="signup-form" role="tab" data-toggle="tab">注册</a>
              </li>
            </ul>
            <div class="tab-content">
              <div role="tabpanel" class="tab-pane active" id="signin-form">
                <form action="/login" method="post">
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-envelope" style="margin:0;"></i>
                      </div>
                      <input type="email" name="login" class="form-control" placeholder="请输入邮箱">
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-lock" style="margin:0;"></i>
                      </div>
                      <input type="password" name="password" class="form-control" placeholder="请输入密码">
                    </div>
                  </div>
                  <div class="form-inline verify-code-item" style="display:none;">
                    <div class="form-group">
                      <div class="input-group">
                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">
                      </div>
                    </div>
                    <img class="verify-code" src="" source="https://www.shiyanlou.com/captcha.gif">
                  </div>
                  <div class="form-group remember-login">
                    <input name="remember" type="checkbox" value="y"> 下次自动登录
                    <a class="pull-right" href="../reset_password/index.html">忘记密码？</a>
                  </div>
                  <div class="form-group">
                    <input class="btn btn-primary" name="submit" type="submit" value="进入实验楼">
                  </div>
                  <div class="form-group widget-signin">
                    <span>快速登录</span>
                    <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                    <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>
                    <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>
                    <a href="/auth/github?next="><i class="fa fa-github"></i></a>
                    <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>
                  </div>
                  <div class="form-group error-msg">
                    <div class="alert alert-danger" role="alert"></div>
                  </div>
                </form>
              </div>
              <div role="tabpanel" class="tab-pane" id="signup-form">
                <form action="/register" method="post">
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-envelope" style="margin:0;"></i>
                      </div>
                      <input type="email" name="email" class="form-control" placeholder="请输入邮箱">
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-lock" style="margin:0;"></i>
                      </div>
                      <input type="password" name="password" class="form-control" placeholder="请输入密码">
                    </div>
                  </div>
                  <div class="form-inline">
                    <div class="form-group">
                      <div class="input-group">
                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">
                      </div>
                    </div>
                    <img class="verify-code" src="" source="https://www.shiyanlou.com/captcha.gif">
                  </div>
                  <div class="form-group">

                    <input class="btn btn-primary" name="submit" type="submit" value="注册">
                  </div>
                  <div class="form-group agree-privacy">
                    注册表示您已经同意我们的<a href="../privacy/index.html" target="_blank">隐私条款</a>
                  </div>
                  <div class="form-group widget-signup">
                    <span>快速注册</span>
                    <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                    <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>
                    <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>
                    <a href="/auth/github?next="><i class="fa fa-github"></i></a>
                    <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>
                  </div>
                  <div class="form-group error-msg">
                    <div class="alert alert-danger" role="alert"></div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <footer1></footer1>
  </div>
</template>

<script>
    import header1 from '@/components/header1'
    import footer1 from '@/components/footer1'
    import {send, sendToken} from '../../static/js/comm'
    import axios from 'axios'

    export default {
        name: "BootCamp",
        data() {
            return {
                bootcampList: [],
                courses: [],
                countDownList: '',
                actEndTime: '2018-11-19 18:50:00',
                pay_type: 1,
                buyWhat: {},
                user_id: localStorage.getItem('user_id')
            }
        },
        created() {


        },
        components: {
            header1: header1,
            footer1: footer1,
        },
        mounted() {
            axios.get('/api/sk/', {}).then((res) => {
                if (res.data.code == 200) {
                    this.courses = res.data.courses;
                    this.courses.forEach((key) => {
                        this.countDown(key)
                    });
                }
            });

        },
        methods: {
            sk: function (i) {
                $('#modal-message').modal('show')
                this.buyWhat = i
            },
            buy: function (i) {
                sendToken('/api/sk/', 'post', {
                    'pay_type': this.pay_type,
                    'user_id': localStorage.getItem('user_id'),
                    'course_id': i.act + ',' + i.time + ',' + i.course
                }).then((res) => {
                    if (res.data.order_number != undefined) {
                        send('/api/pay/?courseOrder_sn=' + res.data.order_number, 'get').then(
                        ).then((res) => {
                            if (res.data.code == 200) {
                                window.location.href = res.data.path
                            }
                        })
                    }
                })
            },
            timeFormat(param) {
                return param < 10 ? '0' + param : param;
            },
            countDown(it) {
                var interval = setInterval(() => {
                    // 获取当前时间，同时得到活动结束时间数组
                    let newTime = new Date().getTime();
                    // 对结束时间进行处理渲染到页面

                    let endTime = new Date(it['date'] + ' ' + it['start']).getTime();
                    let obj = null;
                    // 如果活动未结束，对时间进行处理
                    if (endTime - newTime > 0) {
                        let time = (endTime - newTime) / 1000;
                        // 获取天、时、分、秒
                        let day = parseInt(time / (60 * 60 * 24));
                        let hou = parseInt(time % (60 * 60 * 24) / 3600);
                        let min = parseInt(time % (60 * 60 * 24) % 3600 / 60);
                        let sec = parseInt(time % (60 * 60 * 24) % 3600 % 60);
                        obj = {
                            day: this.timeFormat(day),
                            hou: this.timeFormat(hou),
                            min: this.timeFormat(min),
                            sec: this.timeFormat(sec)
                        };
                    } else { // 活动已结束，全部设置为'00'
                        obj = {
                            day: '00',
                            hou: '00',
                            min: '00',
                            sec: '00'
                        };
                        clearInterval(interval);
                    }
                    it['update_time'] = obj.hou + '时' + obj.min + '分' + obj.sec + '秒';
                }, 1000);
            }
        },

    }
</script>

<style scoped>

</style>
