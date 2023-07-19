export interface PaperInfo {
  author: string;
  title: string;
  detail: string;
  pdf: string;
  categories: string;
}

export interface AIAnswer {
  answer: string;
  papers: PaperInfo[];
}
