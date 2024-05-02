import { Button, Input } from "@nextui-org/react";
import { useMutation } from "@tanstack/react-query";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "sonner";

function IndexPage() {
    const navigate = useNavigate();
    const [teamCode, setTeamCode] = useState<string>("");

    const checkTeamCodeMutation = useMutation({
        mutationFn: () =>
            fetch("http://localhost:8000/api/teams/checkCode", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ code: teamCode }),
            }).then(async (res) => {
                if (!res.ok) {
                    throw new Error(await res.text());
                }
                return res.json();
            }),
        onSuccess: async (data) => {
            navigate(`/team/${data.teamId}`);
        },
        onError: (error) => {
            const message = JSON.parse(error.message);
            console.log(message);
            if (message.detail === "TEAM_CODE_NOT_FOUND")
                toast.error(`很抱歉，但我們找不到這個隊伍！`);
            else
                toast("未知的錯誤發生了！請尋找課活團隊求助", {
                    description: message,
                });
        },
    });

    return (
        <>
            <div className="fixed inset-0 flex justify-center items-center bg-zinc-900">
                <div className="w-full max-w-6xl flex items-center text-white">
                    <div>
                        <h1 className="text-8xl font-semibold">
                            Scribble <br /> Showdown
                        </h1>
                        <form
                            className="mt-4 flex items-center justify-between gap-3"
                            onSubmit={(e) => {
                                e.preventDefault();
                                if (teamCode.length === 0) return;
                                checkTeamCodeMutation.mutate();
                            }}
                        >
                            <Input
                                value={teamCode}
                                onChange={(e) =>
                                    setTeamCode(e.currentTarget.value)
                                }
                                placeholder="輸入團隊登入碼"
                            />
                            <Button
                                type="submit"
                                isLoading={checkTeamCodeMutation.isPending}
                                disabled={teamCode.length === 0}
                            >
                                登入
                            </Button>
                        </form>
                    </div>
                </div>
            </div>
        </>
    );
}

export default IndexPage;
