% Call:
%
%   matlab.engine.shareEngine
% 
% to setup shared engine with python

function [u] = FLS(UserRating, GenreRating)

   %a = newfis('Prototype');
   a = readfis('Prototype.fis');

    %Input 1 (Rated by user)
%     a = addvar(a,'input','userRating',[1 10]);
% 
%     a = addmf(a,'input',1,'disliked','trapmf',[0 0 4 5]);
%     a = addmf(a,'input',1,'indifferent','trimf',[4 5 6]);
%     a = addmf(a,'input',1,'liked','trapmf',[5 7 8 9]);
%     a = addmf(a,'input',1,'loved','trapmf',[8 9 10 10]);
% 
%     % Input 2 (Genre membership)
%     a = addvar(a,'input','genreRating',[0 1]);
% 
%     a = addmf(a,'input',2,'low','gaussmf',[0.25 0]);
%     a = addmf(a,'input',2,'medium','gaussmf', [0.1 0.5]);
%     a = addmf(a,'input',2,'high','gaussmf', [0.25 1]);
% 
%     % Output (preference)
%     a = addvar(a,'output','preference',[1 10]);
% 
%     a = addmf(a,'output',1,'non-preffered','trapmf',[0 0 3 5]);
%     a = addmf(a,'output',1,'indifferent','trimf',[3 5 7]);
%     a = addmf(a,'output',1,'interestedIn','trapmf',[5 7 8 8.5]);
%     a = addmf(a,'output',1,'preffered','trapmf',[6 9 11 14]);
% 
%     % input1, input2, output, weight, operator(1=AND, 2=OR)
%     rule1 = [1 1 2 1 1];
%     a = addrule(a,rule1);
%     rule2 = [1 2 1 1 1];
%     a = addrule(a,rule2);
%     rule3 = [1 3 1 1 1];
%     a = addrule(a,rule3);
%     rule4 = [2 3 2 1 1];
%     a = addrule(a,rule4);
%     rule5 = [2 2 2 1 1];
%     a = addrule(a,rule5);
%     rule6 = [2 1 1 0.2 1];
%     a = addrule(a,rule6);
%     rule7 = [3 3 3 1 1];
%     a = addrule(a,rule7);
%     rule8 = [3 2 3 0.8 1];
%     a = addrule(a,rule8);
%     rule9 = [3 1 2 1 1];
%     a = addrule(a,rule9);
%     rule10 = [4 3 4 1 1];
%     a = addrule(a,rule10);
%     rule11 = [4 2 4 0.8 1];
%     a = addrule(a,rule11);
%     rule12 = [4 1 2 1 1];
%     a = addrule(a,rule12);

    % calculate output
    FLS_input = [UserRating, GenreRating];
    u = evalfis(FLS_input,a);
    
    % display parts of system
    
%     fuzzy(a)
%     mfedit(a)
%     ruleedit(a) 
%     ruleview(a)
%     surfview(a)
    
end
