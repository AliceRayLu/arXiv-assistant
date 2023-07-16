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
      <div><text class="title">How to use</text></div>
      <div class="info">
        <ul style="line-height: 3vh">
          <li>Type in what you want to search</li>
          <li>Click the send button</li>
          <li>The answer and papers' links will be shown on screen</li>
        </ul>
      </div>
      <div><text class="title">Note</text></div>
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
        <el-button color="#626aef">clear all history</el-button>
      </div>
    </el-aside>
    <el-main>
      <div style="display: flex; width: 100%">
        <el-input
          placeholder="Type in sentences to search for papers."
          v-model="userInput"
          :prefix-icon="Search"
          style="display: inline-flex"
          clearable
        ></el-input>
        <el-button
          color="#626aef"
          style="display: inline-flex; margin-left: 0.5vw"
          @click="handleSend"
          >Send
        </el-button>
      </div>
      <div :key="isSend">
        <QandA :question="userInput" :is-send="isSend" />
      </div>
    </el-main>
  </el-container>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { Search } from "@element-plus/icons-vue";
import QandA from "@/components/QandA.vue";

const userInput = ref("");
let isSend = ref(false);

const handleSend = () => {
  isSend.value = true;
};

let questions = [] as string[];
let answers = [] as string[];
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
