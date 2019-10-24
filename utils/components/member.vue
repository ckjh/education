<template>
  <div id="member">

    <header1></header1>

    <div class="vip-header layout-no-margin-top" style="min-height:215px;">
      <h1 class="vip-header-title">加入实验楼会员，拥有自己的实验机</h1>
      <h4 class="vip-header-description">精品课程 + 环境保存 + 实验联网 + 会员客户端</h4>
    </div>
    <div class="vip-details">
      <div class="container">
        <div class="row vip-row hidden-xs">
          <div class="vip-item" v-for="item in conditions" v-if="item.amount>0">
            <ul class="list-group">
              <li class="list-group-item"><h4 class="is-adv-vip">{{item.level}}</h4></li>
              <!--              <li class="list-group-item rebate-number" style="padding-bottom: 6px;">-->
              <!--                &lt;!&ndash;                <span class="number-five"><span style="color: #CC584C;font-size: 23px;">5</span> 折</span>&ndash;&gt;-->
              <!--              </li>-->
              <li class="list-group-item item-vip-footer" style="">
                <strong class="vip-price" style="font-size: 15px;display:block;margin-bottom: -7px"><span
                  style="font-size:28px;color:#CC584C">￥{{item.amount}}</span> / {{item.time}}月</strong>
                <!--                <del style="font-size: 12px;color: #999;">原价 1024元</del>-->
                <br>

                <a type="button" class="btn btn-bigger btn-all" href="#vip-modal" data-toggle="modal" data-sign="signin"
                   data-next="/vip" @click="showForm(item)">加入</a>

                <!--                <p style=""> 实验豆可抵扣现金</p>-->
              </li>
              <ul>
              </ul>
            </ul>
          </div>
        </div>

        <div class="row visible-xs">
          <div class="col-md-4">
            <div class="vip-details-item">
              <div class="vip-details-header is-free-user">
                <h4>免费</h4>
              </div>
              <div class="vip-details-body">
                <div class="vip-details-content">
                  <div>免费课程 <span class="glyphicon glyphicon-ok"></span></div>
                  <div>实验结束后环境删除 <span class="glyphicon glyphicon-ok"></span></div>
                  <div>连接内网 <span class="glyphicon glyphicon-ok"></span></div>
                  <div class="disabled">会员课程 <span class="glyphicon glyphicon-remove"></span></div>
                  <div class="disabled">可保存实验环境 <span class="glyphicon glyphicon-remove"></span></div>
                  <div class="disabled">连接互联网 <span class="glyphicon glyphicon-remove"></span></div>
                  <div class="disabled">会员客户端 <span class="glyphicon glyphicon-remove"></span></div>
                  <div></div>
                </div>
                <div class="vip-details-price is-free-user" style="margin-top: 10px;margin-bottom:21px">
                  <strong>免费</strong>
                </div>
              </div>
              <div class="vip-details-footer is-free-user" style="padding:28px 0 58px 0;">

                <a class="btn btn-primary" href="#sign-modal" data-toggle="modal" data-sign="signup">立即注册</a>

              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
    <div class="vip-hots">
      <div class="container">
        <div class="vip-hots-header">
          <h4>已有 <span>350,000</span> 人在实验楼完成了 <span>6,000,000+</span> 次实验</h4>
        </div>
        <div class="row vip-hots-body">
          <div class="col-md-4">
            <div class="media">
              <div class="media-left">
                <img class="media-object" src="../../static/img/vip-allcourses.png">
              </div>
              <div class="media-body">
                <h4 class="media-heading">课程畅学</h4>
                <p>会员专属精品课程，每周不断更新，给你最快的成长</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="media">
              <div class="media-left">
                <img class="media-object" src="../../static/img/vip-24.png">
              </div>
              <div class="media-body">
                <h4 class="media-heading">随时实践</h4>
                <p>独享实验机，长期保存，在线开发代码，24小时随时继续</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="media">
              <div class="media-left">
                <img class="media-object" src="../../static/img/vip-internet.png">
              </div>
              <div class="media-body">
                <h4 class="media-heading">优质体验</h4>
                <p>环境联网，会员客户端+SSH直连+WebIDE，更优实验体验</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="vip-clients" id="vip-clients">
      <div class="container">
        <div class="vip-clients-header">
          <h4>即开即用的会员客户端，随时随地远程访问实验桌面</h4>
        </div>
        <div class="row vip-clients-body">
          <div class="col-md-4">
            <div class="vip-clients-windows vip-clients-logo"></div>
            <div class="vip-clients-title">Windows - Windows 7 及以上</div>
            <a href="http://labfile.oss-cn-hangzhou.aliyuncs.com/shiyanlou_desktop/shiyanlou-desktop-v1.0.3-win64.exe">立即下载（64位）</a><br/><a
            href="http://labfile.oss-cn-hangzhou.aliyuncs.com/shiyanlou_desktop/shiyanlou-desktop-v1.0.3-win32.exe">立即下载（32位）</a>
            <div class="text-danger" style="font-size:14px;">（安装过程中如果遇到 360 的警告可以忽视）</div>
          </div>
          <div class="col-md-4">
            <div class="vip-clients-mac vip-clients-logo"></div>
            <div class="vip-clients-title">MacOS - MacOS 10.11 及以上</div>
            <a href="http://labfile.oss-cn-hangzhou.aliyuncs.com/shiyanlou_desktop/shiyanlou-desktop-v1.0.3-macos.dmg">立即下载</a>
          </div>
          <div class="col-md-4">
            <div class="vip-clients-linux vip-clients-logo"></div>
            <div class="vip-clients-title">Linux - Ubuntu 14.04 及以上</div>
            <a
              href="http://labfile.oss-cn-hangzhou.aliyuncs.com/shiyanlou_desktop/shiyanlou-desktop-v1.0.3-linux64.deb">立即下载（64位）</a><br/><a
            href="http://labfile.oss-cn-hangzhou.aliyuncs.com/shiyanlou_desktop/shiyanlou-desktop-v1.0.3-linux32.deb">立即下载（32位）</a>
          </div>
          <div class="video">
            <video controls="controls">
              <source src="http://labfile.oss-cn-hangzhou.aliyuncs.com/shiyanlou_desktop/desktop.ogg" type="video/ogg">
              <source src="http://labfile.oss-cn-hangzhou.aliyuncs.com/shiyanlou_desktop/desktop.mp4" type="video/mp4">
              你的浏览器不支持播放视频
            </video>
            <div class="video-play">
              <i class="fa fa-play-circle-o fa-2x"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="vip-faq">
      <div class="container">
        <div class="vip-faq-header">
          <img src="../../static/img/vip-faq.png">
          FAQ
          <span></span>
        </div>
        <div class="vip-faq-body">
          <h4>会员课程和免费课程有什么区别？</h4>
          <div>1. 会员课程多为项目课，免费课程多为基础课。</div>
          <div>2. 会员课程主要由实验楼团队制作及维护，免费课程由实验楼及合作伙伴共同维护。</div>
          <div>3. 会员可联网并保存环境，会员课程内容不受网络及时间限制。</div>
          <div>4. 会员课程更新频率更高，难度会更大。</div>
        </div>
        <div class="vip-faq-body">
          <h4>会员客户端是什么？</h4>
          <div>实验楼会员专属的桌面端软件，即开即用，自动连接云端实验桌面，特点:</div>
          <div>1. 易用：即开即用，随时远程访问实验桌面</div>
          <div>2. 安全：数据云端保存，HTTPS加密传输</div>
          <div>3. 跨平台：支持Windows，Mac OSX 及 Linux平台</div>
          <div>4. 更多功能：实验工具中提供查看文档及一键SSH连接实验环境等</div>
        </div>
        <div class="vip-faq-body">
          <h4>什么情况下需要保存实验环境？</h4>
          <div>1. 当时间不多或实验耗时较长，无法连续完成一个实验时。</div>
          <div>2. 当实验遇到问题但无法及时解决时。</div>
          <div>3. 当需要一台在线开发环境时。</div>
        </div>
        <div class="vip-faq-body">
          <h4>环境联网有什么好处？</h4>
          <div>1. 实验中随时连接站外资源，例如Github等。</div>
          <div>2. 支持大量联网课程，例如微信微博开发及SaaS开发。</div>
        </div>
        <div class="vip-faq-body">
          <h4>成功购买会员服务后，是否可以退款？</h4>
          <div>支付购买成功后，暂不接受退款申请，请详细查看会员服务内容后进行购买，如有任何不清楚的地方欢迎在 <a href="/questions/">讨论区</a> 发帖询问。</div>
        </div>
        <div class="vip-faq-body">
          <h4>高级会员与普通会员有什么不同？</h4>
          <div>1. 实验楼提供专职助教，在讨论区为高级会员提供答疑服务，回答学习会员课程过程中遇到的问题。</div>
          <div>2. 购买训练营享受5折优惠。</div>
        </div>
        <div class="vip-faq-footer">
          <a href="/questions/1440">更多疑问，查看这里></a>
        </div>
      </div>
    </div>
    <div class="modal fade" id="invite-user" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span
              class="sr-only">Close</span></button>
            <h4 class="modal-title">邀请好友，双方都可获赠实验豆！</h4>
          </div>
          <div class="modal-body">

            <p><h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！</h4>

            <div id="msg-modal"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="flash-message" tabindex="-1" role="dialog">
      <div class="modal-dialog" rolw="document">
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
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary confirm" data-dismiss="modal">确定</button>
          </div>
        </div>
      </div>
    </div>


    <div class="modal fade" id="vip-modal" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">加入会员</h4>
            <div class="alert-message">
              <div class="alert alert-danger"></div>
            </div>
          </div>
          <div class="modal-body">
            <div class="vip-modal-item ">
              <div class="vip-modal-item-header">邀请码
                <div class="btn btn-default navbar-btn" @click="useCode=true" v-if="useCode==false">使用</div>
                <div class="btn btn-default navbar-btn" @click="useCode=false" v-if="useCode==true">不使用</div>
              </div>

              <div class="vip-modal-item-body">
                <div class="input-group" v-show="useCode==true">
                  <input type="text" class="form-control phone-number"
                         value="" v-model="invitation_code"
                  >

                </div>
              </div>
            </div>


            <div class="vip-modal-item">
              <div class="vip-modal-item-header">使用积分<span>（最高使用100个积分）
                <div class="btn btn-default navbar-btn" @click="useScore=true" v-if="useScore==false">使用</div>
                <div class="btn btn-default navbar-btn" @click="useScore=false" v-if="useScore==true">不使用</div></span>
              </div>
              <div class="vip-modal-item-body">
                <div class="consume-beans" v-show="useScore==true">
                  <!--                  <input type="checkbox">-->
                  <!--                  <span @click="useScore=true">使用</span>-->
                  <!--                  <span @click="useScore=false">不使用</span>-->
                  <span>使用</span>
                  <input class="form-control" type="text" v-show="useScore" value="0" v-model="num">
                  <span>{{num}}积分抵扣</span>
                  <span class="beans">{{money}}</span>
                  <span>元</span>
                  <div class="left-beans">
                    <div>您的积分还剩 <strong>{{userInfo.integral}}</strong> 个</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="vip-modal-item">
              <div class="vip-modal-item-header">支付方式</div>
              <div class="vip-modal-item-body">
                <div class="pay-method pay-method-ali active" data-pay="ALI_WEB">
                </div>
                <div class="pay-method pay-method-wx" data-pay="WX_NATIVE">
                </div>
              </div>
            </div>
          </div>
          <div class="modal-body vip-modal-qrcode" style="display:none;">
            <div class="vip-wx-price">付款：<span></span></div>
            <div class="vip-wx-qrcode"></div>
            <a class="vip-wx-method" href="javascript:;">更换支付方式</a>
          </div>
          <div class="modal-footer">
            <div class="pull-left real-price">
              <div>
                <div style="float:left"><span>付款：</span><strong>￥</strong><strong class="last-price">{{addForm.amount-money}}</strong>
                </div>
                <br class="__web-inspector-hide-shortcut__">

              </div>


            </div>
            <div class="pull-right pay-btn">
              <a class="btn btn-warning" href="#" @click="buyMember()" v-show="f==false">确认购买</a>
              <a class="btn btn-warning" :href="payUrl" v-show="f">去支付</a>

              <input type="checkbox" checked>
              <span>同意<a href="/terms" target="_blank">会员服务条款</a></span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="paid-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title" style="text-align:center;">支付确认</h4>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col-md-6">
                <button class="btn btn-primary paid-confirm" type="button">支付成功</button>
              </div>
              <div class="col-md-6">
                <button class="btn btn-primary paid-method" type="button" style="background:none; color:#0c9">选择支付方式
                </button>
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
    import {send, sendToken} from '../../static/js/comm'
    import header1 from './header1'
    import footer1 from './footer1'

    export default {
        name: "member",
        num: {
            handler() {
            }
        },
        data() {
            return {
                conditions: [],
                addForm: {},
                rule: 0,
                num: 0,
                useScore: false,
                userInfo: {},
                useCode: false,
                pay_type: 1,
                invitation_code: '',
                payUrl: '',
                f: false
            }
        }, components: {
            header1: header1,
            footer1: footer1,
        }, methods: {
            showForm: function (n) {
                this.addForm = n;
                this.num = 0
            },
            buyMember: function () {
                // alert(this.money)
                if (this.useScore == false) {
                    this.num = 0
                }
                ;
                if (this.useCode == false) {
                    this.invitation_code = ''
                }
                sendToken('/api/memberOrder/', 'post', {
                    'user_id': this.userInfo.id,
                    'level_id': this.addForm.level_id,
                    'num': this.num,
                    'pay_type': this.pay_type,
                    'invitation_code': this.invitation_code
                }).then((res) => {
                    if (res.data.code == 200) {
                        send('/api/pay/?memberOrder_sn=' + res.data.order_sn, 'get').then(
                        ).then((res) => {
                            if (res.data.code == 200) {
                                this.f = true;
                                this.payUrl = res.data.path;
                                window.location.href = res.data.path;

                            }
                        })
                    } else {
                        alert('订单提交失败')
                    }
                })
            }
        }, mounted() {
            sendToken('/api/user/?user_id=' + localStorage.getItem('user_id'), 'get').then((res) => {
                if (res.data.code == 200) {
                    this.userInfo = res.data.userInfo
                } else {
                    alert(res.data.message)
                }
            })
            send('/api/admin01/condition/?p=1', 'get').then((res) => {
                if (res.data.code == 200) {
                    this.conditions = res.data.conditions
                }
            })
            send('/api/admin01/rule/', 'get').then((res) => {
                if (res.data.code == 200) {
                    this.rule = res.data.rule
                }
            })
        },
        computed: {//当数据发生改变时，会自动去计算
            money: function () {
                if (this.num < 100) {
                    var a;
                    a = this.num / this.rule * 1
                    return a;
                } else if (this.num > this.userInfo.integral) {
                    return 0
                } else {
                    return 0
                }
            }
        }
    }
</script>

<style scoped>

</style>
