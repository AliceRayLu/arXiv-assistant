<template>
  <el-container
    style="position: absolute; top: 0; right: 0; bottom: 0; left: 0"
  >
    <el-aside width="20%" style="background-color: #000000; height: 100vh">
      <el-row type="flex" justify="center" align="middle">
        <text style="color: #626aef; font-size: 4vh; margin-top: 2vh">
          arXiv-assistant
        </text>
      </el-row>
      <div style="margin: 2vh 1vw 2vh 1vw">
        <text class="info">
          Using Large Language Model(LLM) to better search papers in arXiv.
        </text>
      </div>
      <div><text class="title">💡 How to use</text></div>
      <div class="info">
        <ul style="line-height: 3vh">
          <li>Type in what you want to search</li>
          <li>Click the send button or press ENTER</li>
          <li>The answer and papers' links will be shown on screen</li>
        </ul>
      </div>
      <div><text class="title">🔔 Note</text></div>
      <div class="info" style="margin: 2vh 1vw 2vh 1vw; line-height: 3vh">
        The searching history will be stored in your browser.<br />
        Click the button below to clear all history.
      </div>
      <div
        style="
          position: absolute;
          bottom: 2vh;
          left: 10%;
          transform: translate(-50%);
        "
      >
        <el-button color="#626aef" @click="clearHistory">
          clear all history
        </el-button>
      </div>
    </el-aside>
    <el-main style="overflow: hidden">
      <div style="display: flex; width: 100%">
        <el-input
          placeholder="Press enter to search."
          v-model="userInput"
          :prefix-icon="Search"
          style="display: inline-flex"
          clearable
          v-on:keyup.enter="handleSend"
          ref="inputEl"
        ></el-input>
        <el-button
          color="#626aef"
          style="display: inline-flex; margin-left: 0.5vw"
          @click="handleSend"
          >Send
        </el-button>
      </div>
      <el-scrollbar :max-height="height" :key="count">
        <div v-for="(ques, index) in questions" v-bind:key="index">
          <div :key="isLoading">
            <QandA :question="ques" :answer="answers[index]" />
          </div>
        </div>
        <div style="height: 3vh" />
      </el-scrollbar>
    </el-main>
  </el-container>
</template>

<script lang="ts" setup>
import { onMounted, ref } from "vue";
import { Search } from "@element-plus/icons-vue";
import QandA from "@/components/QandA.vue";
import { request } from "@/utils/request";
import { AIAnswer, PaperInfo } from "@/utils/paperInfo";

const inputEl = ref();
const height = ref(0);
const userInput = ref("");
let count = ref(0);
let questions = [] as string[];
let answers = [] as AIAnswer[];
let tmp: AIAnswer = {
  answer: "",
  papers: [] as PaperInfo[],
};
const loadingAns: AIAnswer = {
  answer: "Loading...",
  papers: [] as PaperInfo[],
};
let isLoading = ref(0);

onMounted(() => {
  height.value = window.innerHeight - inputEl.value?.clientHeight;
  console.log(height.value);
  const tmpQ = localStorage.getItem("questions");
  const tmpA = localStorage.getItem("answers");
  questions = tmpQ ? JSON.parse(tmpQ) : ([] as string[]);
  answers = tmpA ? JSON.parse(tmpA) : ([] as AIAnswer[]);
  console.log("onmount");
  console.log(answers);
});

const handleSend = () => {
  console.log("handle");
  count.value++;
  questions.splice(0, 0, userInput.value);
  answers.splice(0, 0, loadingAns);
  getAnswer(userInput.value);
  inputEl.value.clear();
};

const getAnswer = (ques: string) => {
  request({
    url: `/search/${ques}`,
    method: "GET",
  })
    .then((res) => {
      console.log(res);
      tmp.answer = res.data.answer;
      tmp.papers = res.data.paperInfo.map((info: PaperInfo) => {
        let i: PaperInfo = {
          title: info.title,
          author: info.author,
          detail: info.detail,
          pdf: info.pdf,
          categories: info.categories,
        };
        return i;
      });
      console.log("this is tmp");
      console.log(tmp);
      answers.splice(0, 1, tmp);
      console.log(answers);
      localStorage.setItem("questions", JSON.stringify(questions));
      localStorage.setItem("answers", JSON.stringify(answers));
      isLoading.value++;
    })
    .catch((error) => {
      console.log(error);
    });
};

const clearHistory = () => {
  localStorage.clear();
  count.value = 0;
  location.reload();
};
</script>

<style>
.info {
  color: #ffffff;
  font-size: small;
}
.title {
  color: #ffffff;
  margin-left: 1vw;
}
</style>
