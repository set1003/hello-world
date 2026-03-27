# Claude Skills 목록

> 새 스킬 추가 시 이 파일에 계속 업데이트할 것.
> 스킬 파일 위치: `C:/Users/micha/.claude/skills/<스킬이름>/SKILL.md`

---

## 등록된 스킬

### `/git-push`
- **파일:** `~/.claude/skills/git-push/SKILL.md`
- **설명:** 변경된 파일을 GitHub에 커밋 후 push
- **트리거:** "push해줘", "커밋하고 올려줘", `/git-push`
- **기능:**
  - `git status` 로 변경 파일 확인
  - `package.json` 있으면 patch 버전 자동 증가
  - `.env` 등 민감 파일 제외하고 선택적 `git add`
  - 한국어 커밋 메시지 자동 작성
  - `main`/`master` force push 금지

---

## 스킬 추가 방법

1. `C:/Users/micha/.claude/skills/<스킬이름>/` 폴더 생성
2. `SKILL.md` 파일 작성:
   ```markdown
   ---
   name: 스킬이름
   description: 언제 이 스킬을 쓸지 설명
   ---

   # 스킬 내용
   Claude에게 줄 지침 작성
   ```
3. 이 파일(SKILLS.md)에 항목 추가

---

## 예정 스킬 (아이디어)

- `/build` — C 파일 컴파일 및 실행
- `/deploy` — GitHub Pages 배포
- `/review` — 코드 리뷰 요청
